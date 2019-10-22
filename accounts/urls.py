from django.urls import path
from accounts.views import TransactionListView

urlpatterns = [
    path('transactions', TransactionListView.as_view(), name='transaction_logs'),
]
