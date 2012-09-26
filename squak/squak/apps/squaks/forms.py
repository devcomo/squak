"""
Squak forms.
"""

from django import forms

from squak.apps.squaks import models


class SquakForm(forms.ModelForm):
    """
    Squak form.
    """
    class Meta:
        model = models.Squak
        fields = ('text', )

    def __init__(self, **kwargs):
        """
        Dynamically set the squak owner
        """
        owner = kwargs.pop('owner')
        super(SquakForm, self).__init__(**kwargs)

        self.instance.owner = owner
