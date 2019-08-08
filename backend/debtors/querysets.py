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
        result = self.select_related('invoices')
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

        print(filters)

        return self.filter(**filters)


class InvoiceQuerySet(models.QuerySet):
    def custom_filter(self, debtor_email=None, invoice_status=None, amount=None, due_date=None, orderby=None):
        result = self.select_related('invoices')
        filters = {}

        if debtor_email:
            filters['debtor__email'] = debtor_email

        if invoice_status:
            filters['status'] = invoice_status

        if amount:
            filters['amount'] = amount

        if due_date:
            filters['due_date'] = due_date

        result = self.filter(**filters)

        if orderby:
            result = result.order_by(orderby)

        return result