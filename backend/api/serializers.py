from rest_framework import serializers

from .models import Debtor, Invoice


class DebtorSerializer(serializers.ModelSerializer):
    open_invoices_count = serializers.ReadOnlyField()
    overdue_invoices_count = serializers.ReadOnlyField()
    paid_invoices_count = serializers.ReadOnlyField()

    class Meta:
        model = Debtor
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'