import requests
import csv
from django.conf import settings
from requests.auth import AuthBase
from django.http import HttpResponse

class PaystackAuth(AuthBase):
    """Implements a custom authentication scheme for paystack."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['Authorization'] = f'Bearer {self.token}'  
        return r


def verify_payment(reference):
    pass



def export_as_csv_action(description="Export selected objects as CSV file", fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        #     field_names = field_names - excludeset

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format('Investors-list')

        writer = csv.writer(response)

        if header:
            writer.writerow(list(fields))
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in fields])

        return response

    export_as_csv.short_description = description
    return export_as_csv
