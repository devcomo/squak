"""
Identity models.
"""

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Identity(models.Model):
    """
    A users identity
    """
    user = models.OneToOneField(User)
    photo = models.ImageField(_('Photo'),
        upload_to='photos', blank=True, null=True)
    bio = models.CharField(_('Bio'), max_length=280, blank=True, null=True)

    def __unicode__(self):
        return self.user.username
