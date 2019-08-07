from django.contrib.auth import get_user_model

from django.db import models

from django.utils.translation import ugettext_lazy as _

from .fields import IBANField
User = get_user_model()


        
class Debtor(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    iban = IBANField()

    admin_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_debtors')

    def __str__(self):
        return f'{self.first_name} {self.last_name} IBAN: {self.iban}'


class Invoice(models.Model):
    OPEN = '0'
    OVERDUE = '1'
    PAID = '2'
    STATUS_CHOICES = (
        (OPEN, _('Open')),
        (OVERDUE, _('Overdue')),
        (PAID, _('Paid')),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=OPEN, blank=False)
    amount = models.IntegerField(blank=False)
    due_date = models.DateField(blank=False)
    
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE, related_name='invoices')

    def __str__(self):
        return f'Amount: {self.amount} Debtor: {self.debtor.first_name}'
    