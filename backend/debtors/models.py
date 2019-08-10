from django.contrib.auth import get_user_model

from django.db import models

from django.utils.translation import ugettext_lazy as _

from localflavor.generic.models import IBANField

from .querysets import DebtorQuerySet, InvoiceQuerySet

User = get_user_model()

        
class Debtor(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    iban = IBANField()

    admin_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_debtors')

    objects = DebtorQuerySet.as_manager()

    def is_created_by_admin(self, admin):
        return self.admin_creator == admin

    def __str__(self):
        return f'{self.first_name} {self.last_name} IBAN: {self.iban}'


class Invoice(models.Model):
    OPEN = '0'
    OVERDUE = '1'
    PAID = '2'
    STATUS_CHOICES = (
        (OPEN, _('open')),
        (OVERDUE, _('overdue')),
        (PAID, _('paid')),
    )
    STATUS_CHOICES_DICT = {
        OPEN: 'open',
        OVERDUE: 'overdue',
        PAID: 'paid',
    }
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=OPEN, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    due_date = models.DateField(blank=False)
    
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE, related_name='invoices')

    objects = InvoiceQuerySet.as_manager()

    def is_created_by_admin(self, admin):
        return self.debtor.admin_creator == admin

    def __str__(self):
        return f'Amount: {self.amount} Debtor: {self.debtor.first_name}'
    