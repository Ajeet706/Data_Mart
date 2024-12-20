import logging
from datetime import datetime, timedelta
from django.utils.timezone import now
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout

logger = logging.getLogger(__name__)

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity_str = request.session.get('last_activity')
            if last_activity_str:
                last_activity = datetime.fromisoformat(last_activity_str)
                elapsed_time = now() - last_activity
                logger.info(f"Elapsed time: {elapsed_time}")
                if elapsed_time > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                    logger.info(f"Logging out user: {request.user}")
                    logout(request)
                    return redirect('login')  # Replace 'login' with your login URL name

            request.session['last_activity'] = now().isoformat()

        response = self.get_response(request)
        return response
