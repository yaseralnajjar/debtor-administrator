# src: https://github.com/django/django-localflavor/blob/163785f179e3176bb95aee13005df411ed3509da/localflavor/generic/validators.py

from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.deconstruct import deconstructible

from django.utils.translation import ugettext_lazy as _


IBAN_COUNTRY_CODE_LENGTH = {'AD': 24,  # Andorra
                            'AE': 23,  # United Arab Emirates
                            'AL': 28,  # Albania
                            'AT': 20,  # Austria
                            'AZ': 28,  # Azerbaijan
                            'BA': 20,  # Bosnia and Herzegovina
                            'BE': 16,  # Belgium
                            'BG': 22,  # Bulgaria
                            'BH': 22,  # Bahrain
                            'BR': 29,  # Brazil
                            'BY': 28,  # Republic of Belarus
                            'CH': 21,  # Switzerland
                            'CR': 22,  # Costa Rica
                            'CY': 28,  # Cyprus
                            'CZ': 24,  # Czech Republic
                            'DE': 22,  # Germany
                            'DK': 18,  # Denmark
                            'DO': 28,  # Dominican Republic
                            'EE': 20,  # Estonia
                            'ES': 24,  # Spain
                            'FI': 18,  # Finland
                            'FO': 18,  # Faroe Islands
                            'FR': 27,  # France + French Guiana (GF), Guadeloupe (GP), Martinique (MQ), Réunion (RE),
                                       #          French Polynesia (PF), French Southern Territories (TF), Mayotte (YT),
                                       #          New Caledonia (NC), Saint Barthélemy (BL),
                                       #          Saint Martin - French part (MF), Saint-Pierre and Miquelon (PM),
                                       #          Wallis and Futuna (WF)
                            'GB': 22,  # United Kingdom + Guernsey (GG), Isle of Man (IM), Jersey (JE)
                            'GE': 22,  # Georgia
                            'GI': 23,  # Gibraltar
                            'GL': 18,  # Greenland
                            'GR': 27,  # Greece
                            'GT': 28,  # Guatemala
                            'HR': 21,  # Croatia
                            'HU': 28,  # Hungary
                            'IE': 22,  # Ireland
                            'IL': 23,  # Israel
                            'IQ': 23,  # Iraq
                            'IS': 26,  # Iceland
                            'IT': 27,  # Italy
                            'JO': 30,  # Jordan
                            'KW': 30,  # Kuwait
                            'KZ': 20,  # Kazakhstan
                            'LB': 28,  # Lebanon
                            'LC': 32,  # Saint Lucia
                            'LI': 21,  # Liechtenstein
                            'LT': 20,  # Lithuania
                            'LU': 20,  # Luxembourg
                            'LV': 21,  # Latvia
                            'MC': 27,  # Monaco
                            'MD': 24,  # Moldova
                            'ME': 22,  # Montenegro
                            'MK': 19,  # Macedonia
                            'MR': 27,  # Mauritania
                            'MT': 31,  # Malta
                            'MU': 30,  # Mauritius
                            'NL': 18,  # Netherlands
                            'NO': 15,  # Norway
                            'PK': 24,  # Pakistan
                            'PL': 28,  # Poland
                            'PS': 29,  # Palestine
                            'PT': 25,  # Portugal
                            'QA': 29,  # Qatar
                            'RO': 24,  # Romania
                            'RS': 22,  # Serbia
                            'SA': 24,  # Saudi Arabia
                            'SC': 31,  # Seychelles
                            'SE': 24,  # Sweden
                            'SI': 19,  # Slovenia
                            'SK': 24,  # Slovakia
                            'SM': 27,  # San Marino
                            'ST': 25,  # Sao Tome and Principe
                            'SV': 28,  # El Salvador
                            'TL': 23,  # Timor-Leste
                            'TN': 24,  # Tunisia
                            'TR': 26,  # Turkey
                            'UA': 29,  # Ukraine
                            'VA': 22,  # Vatican
                            'VG': 24,  # British Virgin Islands
                            'XK': 20}  # Kosovo (user-assigned country code)


@deconstructible
class IBANValidator:
    """A validator for International Bank Account Numbers (IBAN - ISO 13616-1:2007)."""

    def __init__(self, use_nordea_extensions=False, include_countries=None):
        self.use_nordea_extensions = use_nordea_extensions
        self.include_countries = include_countries

        self.validation_countries = IBAN_COUNTRY_CODE_LENGTH.copy()
        if self.use_nordea_extensions:
            self.validation_countries.update(NORDEA_COUNTRY_CODE_LENGTH)

        if self.include_countries:
            for country_code in self.include_countries:
                if country_code not in self.validation_countries:
                    msg = 'Explicitly requested country code %s is not ' \
                          'part of the configured IBAN validation set.' % country_code
                    raise ImproperlyConfigured(msg)

    def __eq__(self, other):
        return (self.use_nordea_extensions == other.use_nordea_extensions and
                self.include_countries == other.include_countries)

    @staticmethod
    def iban_checksum(value):
        """
        Returns check digits for an input IBAN number.
        Original checksum in input value is ignored.
        """
        # 1. Move the two initial characters to the end of the string, replacing checksum for '00'
        value = value[4:] + value[:2] + '00'

        # 2. Replace each letter in the string with two digits, thereby expanding the string, where
        #    A = 10, B = 11, ..., Z = 35.
        value_digits = ''
        for x in value:
            if '0' <= x <= '9':
                value_digits += x
            elif 'A' <= x <= 'Z':
                value_digits += str(ord(x) - 55)
            else:
                raise ValidationError(_('%s is not a valid character for IBAN.') % x)

        # 3. The remainder of the number above when divided by 97 is then subtracted from 98.
        return '%02d' % (98 - int(value_digits) % 97)

    def __call__(self, value):
        """
        Validates the IBAN value using the official IBAN validation algorithm.
        https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN
        """
        if value is None:
            return value

        value = value.upper().replace(' ', '').replace('-', '')

        # Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid.
        country_code = value[:2]
        if country_code in self.validation_countries:

            if self.validation_countries[country_code] != len(value):
                msg_params = {'country_code': country_code, 'number': self.validation_countries[country_code]}
                raise ValidationError(_('%(country_code)s IBANs must contain %(number)s characters.') % msg_params)

        else:
            raise ValidationError(_('%s is not a valid country code for IBAN.') % country_code)
        if self.include_countries and country_code not in self.include_countries:
            raise ValidationError(_('%s IBANs are not allowed in this field.') % country_code)

        if self.iban_checksum(value) != value[2:4]:
            raise ValidationError(_('Not a valid IBAN.'))