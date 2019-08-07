from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from rest_framework.test import APITestCase

from .models import Debtor

User = get_user_model()


class DebtorTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.user = User.objects.get(username='testuser')

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
        debtor = Debtor(first_name='tester', last_name='rester', 
                        email='tester@gmail.com', iban='DE75512108001245126199',
                        admin_creator=self.user)
        debtor.save()
        debtor_to_update = Debtor.objects.get(first_name='tester')

        debtor_payload = {
            'first_name': 'new_tester',
        }
        response = self.client.patch(reverse('debtors-detail', args=(debtor_to_update.id,)), 
                                     debtor_payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Debtor.objects.get(id=debtor_to_update.id).first_name, 'new_tester')

    def test_delete_debtor(self):
        debtor = Debtor(first_name='tester', last_name='rester', 
                        email='tester@gmail.com', iban='DE75512108001245126199',
                        admin_creator=self.user)
        debtor.save()
        debtor_to_delete = Debtor.objects.get(first_name='tester')

        response = self.client.delete(reverse('debtors-detail', args=(debtor_to_delete.id,)))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Debtor.objects.filter(id=debtor_to_delete.id).first(), None)
