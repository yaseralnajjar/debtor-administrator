# src: https://github.com/django/django-localflavor/blob/163785f179e3176bb95aee13005df411ed3509da/localflavor/generic/models.py#L8

from django.db import models

from django.utils.translation import ugettext_lazy as _

from .validators import IBANValidator


class IBANField(models.CharField):
    """
    An IBAN consists of up to 34 alphanumeric characters.
    To limit validation to specific countries, set the 'include_countries' argument with a tuple or list of ISO 3166-1
    alpha-2 codes. For example, `include_countries=('NL', 'BE, 'LU')`.
    A list of countries that use IBANs as part of SEPA is included for convenience. To use this feature, set
    `include_countries=IBAN_SEPA_COUNTRIES` as an argument to the field.
    Example:
    .. code-block:: python
        from django.db import models
        from localflavor.generic.models import IBANField
        from localflavor.generic.countries.sepa import IBAN_SEPA_COUNTRIES
        class MyModel(models.Model):
            iban = IBANField(include_countries=IBAN_SEPA_COUNTRIES)
    In addition to validating official IBANs, this field can optionally validate unofficial IBANs that have been
    catalogued by Nordea by setting the `use_nordea_extensions` argument to True.
    https://en.wikipedia.org/wiki/International_Bank_Account_Number
    .. versionadded:: 1.1
    """

    description = _('An International Bank Account Number')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 34)
        self.use_nordea_extensions = kwargs.pop('use_nordea_extensions', False)
        self.include_countries = kwargs.pop('include_countries', None)
        super().__init__(*args, **kwargs)
        self.validators.append(IBANValidator(self.use_nordea_extensions, self.include_countries))

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['use_nordea_extensions'] = self.use_nordea_extensions
        kwargs['include_countries'] = self.include_countries
        return name, path, args, kwargs

    def to_python(self, value):
        value = super().to_python(value)
        if value is not None:
            return value.upper().replace(' ', '').replace('-', '')
        return value

    def formfield(self, **kwargs):
        defaults = {
            'use_nordea_extensions': self.use_nordea_extensions,
            'include_countries': self.include_countries,
            'form_class': IBANFormField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)