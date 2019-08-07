from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from .models import Debtor, Invoice
from .serializers import DebtorSerializer, InvoiceSerializer
from .permissions import CreatedByCurrentAdmin


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))



class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class DebtorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, CreatedByCurrentAdmin)
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).with_invoices_stats()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, CreatedByCurrentAdmin)
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
