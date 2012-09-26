"""
Identity signals
"""

from django.contrib.auth import models as auth_models
from django.db.models.signals import post_save
from .models import Identity


def create_identity(instance, created, **kwargs):
    """
    Create an identity when a user is created.
    """
    if created:
        Identity.objects.get_or_create(user=instance)


post_save.connect(create_identity, sender=auth_models.User)
