from django.urls import path, include

from rest_framework import routers

from .views import index_view, DebtorViewSet, InvoiceViewSet


router = routers.DefaultRouter()
router.register('debtors', DebtorViewSet, base_name='debtors')
router.register('invoices', InvoiceViewSet, base_name='invoices')


urlpatterns = [
    path('', index_view, name='index'),

    # http://localhost:8000/api/debtors
    # http://localhost:8000/api/invoices
    path('api/', include(router.urls)),
]