from rest_auth.registration.views import SocialLoginView

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter