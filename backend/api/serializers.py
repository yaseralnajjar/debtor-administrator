from rest_framework import serializers

from .models import Debtor


class DebtorSerializer(serializers.ModelSerializer):
    open_invoices_count = serializers.IntegerField()
    overdue_invoices_count = serializers.IntegerField()
    paid_invoices_count = serializers.IntegerField()

    class Meta:
        model = Debtor
        fields = '__all__'