PINK = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
REVERSE = '\033[7m'


class PrettyText:
    def __init__(self, message: str):
        self.__message = message

    def __str__(self):
        return self.__message

    def __set_modifier_and_return_self(self, modifier: str):
        self.__message = modifier + self.__message
        if END not in self.__message:
            self.__message += END
        return self

    def pink(self):
        return self.__set_modifier_and_return_self(PINK)

    def blue(self):
        return self.__set_modifier_and_return_self(BLUE)

    def green(self):
        return self.__set_modifier_and_return_self(GREEN)

    def yellow(self):
        return self.__set_modifier_and_return_self(YELLOW)

    def red(self):
        return self.__set_modifier_and_return_self(RED)

    def bold(self):
        return self.__set_modifier_and_return_self(BOLD)

    def underline(self):
        return self.__set_modifier_and_return_self(UNDERLINE)

    def reverse(self):
        return self.__set_modifier_and_return_self(REVERSE)
