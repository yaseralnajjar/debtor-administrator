from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from .models import Debtor
from .serializers import DebtorSerializer
from .permissions import CreatedByCurrentAdmin


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class DebtorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, CreatedByCurrentAdmin)
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer


