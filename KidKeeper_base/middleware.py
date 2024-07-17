# KidKeeper_base/middleware.py
from django.utils.deprecation import MiddlewareMixin


class NoCacheMiddleware(MiddlewareMixin):
    def process_respone(self, request, response):
        response["cache-control"] = "no-cache, no-store, must-revalidate"
        response["pragma"] = "no-cache"
        response["Expires"] = "0"
        return response
