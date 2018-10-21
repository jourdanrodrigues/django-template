class XFrameOptionsMiddleware:
    """
    Middleware to deny use within "frame" or "iframe"
    Customization from "django.middleware.clickjacking.XFrameOptionsMiddleware"
    """
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Frame-Options'] = 'DENY'
        return response
