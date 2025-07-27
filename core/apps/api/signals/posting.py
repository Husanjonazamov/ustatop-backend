from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import PostingModel


@receiver(post_save, sender=PostingModel)
def PostingSignal(sender, instance, created, **kwargs): ...
