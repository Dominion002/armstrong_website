# middleware.py
from django.urls import reverse
from django.shortcuts import redirect
from django.conf import settings

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user'),"The request object should have a 'user' attribute."

        exempt_urls = settings.LOGIN_EXEMPT_URL
        
        # Use reverse to match URL patterns
        exempt_url_paths = [url.lstrip('/') for url in exempt_urls]

  
        if request.path_info.lstrip('/') in exempt_url_paths:
            return None  # Allow the view to proceed without login check

        # Perform the login required check for other URLs
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        print("No conditions matched. Allowing view to proceed.")
        return None
