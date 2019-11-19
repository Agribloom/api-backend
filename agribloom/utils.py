import requests
from django.conf import settings
from requests.auth import AuthBase

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