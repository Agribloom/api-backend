from accounts.models import CustomUser, Transaction
from crowdfund.models import Farm


def update_farm_record(sender, instance, created, **kwargs):
    if created:
        farm = Farm.objects.get(pk=instance.farm.id)
        farm.unit_in_stock = (
            farm.unit_in_stock - instance.units
        )
        farm.raised = (
            farm.raised + instance.amount
        )
        if farm.unit_in_stock == 0:
            farm.status = Farm.PROJECT_SOLD_OUT
        farm.save()


def create_investment_log(sender, instance, created, **kwargs):
    if created:
        transaction = Transaction.objects.create(
            owner=instance.owner,
            farm=instance.farm,
            description='Paid',
            amount=instance.amount,
            status=Transaction.PAID,
            transaction_type=Transaction.PURCHASE

        )
