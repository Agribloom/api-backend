from django.urls import path
from accounts.views import TransactionListView
from crowdfund.views import InvestmentListView

urlpatterns = [
    path('transactions', TransactionListView.as_view(), name='transaction_logs'),
    path("investments", InvestmentListView.as_view(), name="investment")
]
