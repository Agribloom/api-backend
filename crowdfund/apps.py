from django.apps import AppConfig
from django.db.models.signals import post_save
import logging


class CrowdfundConfig(AppConfig):
    name = 'crowdfund'

    def ready(self):
        logging.info('34')
        from crowdfund.models import Investment
        from crowdfund.signals import update_farm_record
        post_save.connect(update_farm_record, sender=Investment)
