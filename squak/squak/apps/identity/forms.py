"""
Identity forms
"""

from django.contrib.auth import models as auth_models
from django import forms
from django.utils.translation import ugettext as _

from squak.apps.identity import models


class EditProfileForm(forms.ModelForm):
    """
    A form to edit a users profile.
    """

    name = forms.CharField(max_length=255, required=True, label=_('Name'))
    email = forms.EmailField(widget=forms.TextInput(),
        max_length=75, required=True, label=_('Email address'))

    class Meta:
        model = models.Identity
        fields = ('photo', 'bio', )

    def __init__(self, **kwargs):
        """
        Dynamically put name/email into this ModelForm from
        the :class:`User` model.
        """
        super(EditProfileForm, self).__init__(**kwargs)

        field = self.fields['name']
        field.initial = self.instance.user.get_full_name()

        field = self.fields['email']
        field.initial = self.instance.user.email

    def clean_email(self):
        """
        Validate the email address
        """
        try:
            email = auth_models.User.objects.get(
                email__iexact=self.cleaned_data['email'])
        except auth_models.User.DoesNotExist:
            return self.cleaned_data['email']

        if email.pk == self.instance.user.pk:
            return self.cleaned_data['email']

        raise forms.ValidationError(_('That email address is taken.'))

    def save(self, commit=True):
        """
        Save the objects
        """
        identity = super(EditProfileForm, self).save(commit=commit)

        # save the users email address
        identity.user.email = self.cleaned_data['email']

        # take care of the first/last name.
        name = self.cleaned_data['name'].split(' ')
        identity.user.first_name = name[0]
        identity.user.last_name = ' '.join(name[1:])
        identity.user.save()

        return identity
