import logging


class Log403Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 403:
            logger = logging.getLogger('django')
            logger.warning(f"403 Forbidden: {request.path} with method {request.method}, user: {request.user}")
        return response
