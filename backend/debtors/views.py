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
    serializer_class = DebtorSerializer

    def get_queryset(self):
        return Debtor.objects\
                     .with_invoices_stats()\
                     .filter_by_invoices(invoice_status=self.request.query_params.get('status', None),
                                         count=self.request.query_params.get('count', None))


class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, CreatedByCurrentAdmin)
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        filters = {
            'debtor__email': self.request.query_params.get('email', None),
            'status': self.request.query_params.get('status', None),
            'amount': self.request.query_params.get('amount', None),
            'due_date': self.request.query_params.get('due_date', None),
        }
        filters = {k:v for k,v in filters.items() if v is not None}

        result = Invoice.objects.filter(**filters)

        orderby = self.request.query_params.get('orderby', None)                                       
        if orderby:
           result = result.order_by(orderby)

        return result