"""
Identity Views.
"""

from django.core.urlresolvers import reverse
from django.views import generic
from squak.apps.identity import forms, models


class EditProfile(generic.edit.UpdateView):
    """
    This view allows editing of a users profile.
    """
    template_name = 'identity/edit-profile.html'
    form_class = forms.EditProfileForm

    def get_object(self):
        """
        Edit the queryset to get the currently logged in user.
        """
        return models.Identity.objects.get(user=self.request.user)

    def get_success_url(self):
        """
        Set the page to redirect to after submitting the form.
        """
        return reverse('user-squak-list',
            kwargs={'username': self.request.user.username})
