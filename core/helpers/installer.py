import os
import platform
from distutils.spawn import find_executable
from subprocess import Popen, PIPE

from .pretty_terminal import PrettyText


def _run(*args):
    return Popen(args, stdout=PIPE, stderr=PIPE)


class Installer:
    system = platform.system()

    def __init__(self, package_name: str):
        self.package_name = package_name

    def _communicate(self, process: Popen) -> tuple:
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            if isinstance(stderr, bytes):
                stderr = stderr.decode('utf-8')

            error_label = 'Something went wrong installing "{}". Here is the output:'.format(self.package_name)

            raise ChildProcessError('{}\n{}'.format(
                PrettyText(error_label).red(),
                PrettyText(stderr).yellow(),
            ))

        return stdout, stderr

    def install(self):
        package_name = self.package_name  # Local variables are faster

        if os.getenv('CI') != 'true':
            print(PrettyText('Installing "{}"...'.format(package_name)).blue())
        else:
            print(PrettyText('Skipping installation of "{}" on CI environment'.format(package_name)).yellow())
            return

        apt_get_bin = find_executable('apt-get')
        if not apt_get_bin:
            print(PrettyText('Skipping since "apt-get" was not found in the system.'.format(package_name)).yellow())
            return

        Popen([apt_get_bin, 'update', '-y']).wait()
        process = _run(apt_get_bin, 'install', '-y', package_name)

        self._communicate(process)

        print(PrettyText('"{}" installed!'.format(package_name)).green())
