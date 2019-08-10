from django.shortcuts import reverse
from django.test import TransactionTestCase

from rest_framework.test import APITestCase

from ..models import Debtor, Invoice

from .factory import create_user, create_debtor, create_invoice


class DebtorTestCase(APITestCase):
    def setUp(self):
        self.user = create_user(username='testuser', password='12345')
        logged_in = self.client.login(username='testuser', password='12345')

    def test_get_debtor(self):
        response = self.client.get(reverse('debtors-list'))
        self.assertEqual(response.status_code, 200)

    def test_post_debtor(self):
        debtor_payload = {
            'first_name': 'tester',
            'last_name': 'rester',
            'email': 'tester@gmail.com',
            'iban': 'AL35202111090000000001234567',
            'admin_creator': self.user.id
        }

        response = self.client.post(reverse('debtors-list'), debtor_payload)
        self.assertEqual(response.status_code, 201)

    def test_put_debtor(self):
        debtor_to_update = create_debtor(admin_creator=self.user)

        debtor_payload = {
            'first_name': 'new_tester',
        }
        response = self.client.patch(reverse('debtors-detail', args=(debtor_to_update.id,)), 
                                     debtor_payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Debtor.objects.get(id=debtor_to_update.id).first_name, 'new_tester')

    def test_put_debtor_not_allowed(self):
        # business logic: if an admin created debtors, other admins can't manipulate them other than the same admin

        another_user = create_user('another_user', '12345')
        debtor_to_update = create_debtor(admin_creator=another_user)

        debtor_payload = {
            'first_name': 'new_tester',
        }
        response = self.client.patch(reverse('debtors-detail', args=(debtor_to_update.id,)), 
                                     debtor_payload)
        self.assertEqual(response.status_code, 403)

    def test_delete_debtor(self):
        debtor_to_delete = create_debtor(admin_creator=self.user)

        response = self.client.delete(reverse('debtors-detail', args=(debtor_to_delete.id,)))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Debtor.objects.filter(id=debtor_to_delete.id).first(), None)


class InvoiceTestCase(APITestCase):
    def setUp(self):
        self.user = create_user(username='testuser', password='12345')
        self.debtor = create_debtor(admin_creator=self.user)

        logged_in = self.client.login(username='testuser', password='12345')

    def test_get_invoice(self):
        response = self.client.get(reverse('invoices-list'))
        self.assertEqual(response.status_code, 200)

    def test_post_invoice(self):
        invoice_payload = {
            'status': Invoice.OPEN,
            'amount': 50000,
            'due_date': '2019-10-10',
            'debtor': self.debtor.id
        }

        response = self.client.post(reverse('invoices-list'), invoice_payload)
        self.assertEqual(response.status_code, 201)

    def test_put_invoice(self):
        invoice_to_update = create_invoice(self.debtor)

        invoice_payload = {
            'amount': '60000',
        }
        response = self.client.patch(reverse('invoices-detail', args=(invoice_to_update.id,)), 
                                     invoice_payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Invoice.objects.get(id=invoice_to_update.id).amount, 60000)

    def test_put_invoice_not_allowed(self):
        # business logic: invoices of debtors could only be manipulate by the same admin who created them

        another_user = create_user('another_user', '12345')
        another_debtor = create_debtor(admin_creator=another_user, first_name='another_debtor_tester')
        invoice_to_update = create_invoice(another_debtor)

        invoice_payload = {
            'amount': '60000',
        }
        response = self.client.patch(reverse('invoices-detail', args=(invoice_to_update.id,)), 
                                     invoice_payload)
        self.assertEqual(response.status_code, 403)

    def test_delete_invoice(self):
        invoice_to_delete = create_invoice(self.debtor)

        response = self.client.delete(reverse('invoices-detail', args=(invoice_to_delete.id,)))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Invoice.objects.filter(id=invoice_to_delete.id).first(), None)