from django.contrib import admin

from .models import Debtor, Invoice


admin.site.register(Debtor)
admin.site.register(Invoice)