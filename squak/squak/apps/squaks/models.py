"""
Squak models
"""

from django.utils.translation import ugettext as _
from django.db import models
from squak.apps.identity import models as identity_models


class Squak(models.Model):
    """
    Squak Model
    """
    owner = models.ForeignKey(identity_models.Identity)
    text = models.CharField(_('Squak text'), max_length=280)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if len(self.text) > 20:
            return u'{0}...'.format(self.text[0:19])
        return self.text[0:19]
