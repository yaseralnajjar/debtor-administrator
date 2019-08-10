import datetime

from django.contrib.auth import get_user_model

from ..models import Debtor, Invoice

User = get_user_model()


def create_user(username, password):
    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
    
    return User.objects.get(username=username)


def create_debtor(admin_creator, first_name='tester'):
    debtor = Debtor(first_name=first_name, last_name='rester', 
                        email='tester@gmail.com', iban='DE75512108001245126199',
                        admin_creator=admin_creator)
    debtor.save()
    
    return Debtor.objects.get(first_name=first_name)


def create_invoice(debtor, status=Invoice.OPEN, amount=50000):
    invoice = Invoice(status, amount=amount, due_date=datetime.date(2019, 10, 10), debtor=debtor)
    invoice.save()

    return Invoice.objects.get(amount=amount)