from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from .models import Message, MessageSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


