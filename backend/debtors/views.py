from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Debtor, Invoice
from .serializers import DebtorSerializer, InvoiceSerializer
from .permissions import CreatedByCurrentAdmin


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class DebtorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, CreatedByCurrentAdmin)
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())\
                       .with_invoices_stats()\
                       .filter_by_invoices(invoice_status=request.query_params.get('status', None),
                                           count=request.query_params.get('count', None))

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
        queryset = self.filter_queryset(self.get_queryset())\
                       .custom_filter(debtor_email=request.query_params.get('email', None),
                                      invoice_status=request.query_params.get('status', None),
                                      amount=request.query_params.get('amount', None),
                                      due_date=request.query_params.get('due_date', None),
                                      orderby=request.query_params.get('orderby', None))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
