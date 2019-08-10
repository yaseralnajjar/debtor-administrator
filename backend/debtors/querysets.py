from django.db import models


class DebtorQuerySet(models.QuerySet):
    OPEN = '0'
    OVERDUE = '1'
    PAID = '2'
    STATUS_CHOICES_DICT = {
        OPEN: 'open',
        OVERDUE: 'overdue',
        PAID: 'paid',
    }

    def with_invoices_stats(self):
        count_open_invoices_query = models.Count('invoices', filter=models.Q(invoices__status=DebtorQuerySet.OPEN))
        count_overdue_invoices_query = models.Count('invoices', filter=models.Q(invoices__status=DebtorQuerySet.OVERDUE))
        count_paid_invoices_query = models.Count('invoices', filter=models.Q(invoices__status=DebtorQuerySet.PAID))
        result = self.annotate(open_invoices_count=count_open_invoices_query,
                               overdue_invoices_count=count_overdue_invoices_query,
                               paid_invoices_count=count_paid_invoices_query)

        return result

    def filter_by_invoices(self, invoice_status=None, count=None):
        filters = {}

        if invoice_status:
            filters['invoices__status'] = invoice_status

        if count:
            invoice_status_string = DebtorQuerySet.STATUS_CHOICES_DICT[invoice_status]
            count_field_name = f'{invoice_status_string}_invoices_count'
            filters[count_field_name] = count

        return self.filter(**filters)