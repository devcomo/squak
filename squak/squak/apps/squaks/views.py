"""
Squak views.
"""

from django import http
from django.core.urlresolvers import reverse
from django.views import generic

from squak.apps.squaks import models, forms
from squak.apps.identity import models as identity_models


class HomePage(generic.TemplateView):
    """
    Homepage.
    """
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            return http.HttpResponseRedirect(reverse('global-squak-list'))
        return super(HomePage, self).get(request, *args, **kwargs)


class CreateSquak(generic.edit.CreateView):
    """
    Create a squak
    """
    template_name = 'squak/create.html'
    model = models.Squak
    form_class = forms.SquakForm

    def get_success_url(self):
        """
        Set the page to redirect to after submitting the form.
        """
        return reverse('user-squak-list',
            kwargs={'username': self.request.user.username})

    def get_form_kwargs(self, **kwargs):
        """
        Pass owner to the form class
        """
        kwargs = super(CreateSquak, self).get_form_kwargs(**kwargs)
        kwargs['owner'] = self.request.user.identity
        return kwargs


class SquakList(generic.ListView):
    """
    List squaks either globally or per user.
    """

    template_name = 'squak/list.html'
    model = models.Squak
    context_object_name = 'squaks'
    user = None

    def get_queryset(self):
        """
        Filter either globally or per-user
        """
        username = self.kwargs.get('username')

        if username:
            self.template_name = 'squak/user-squak-list.html'
            # does this identity exist?
            try:
                self.user = identity_models.Identity.objects\
                    .get(user__username__iexact=username)
            except identity_models.Identity.DoesNotExist:
                raise http.Http404

            return self.model.objects.filter(owner__user=self.user)

        # no username, get them all.
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        """
        Return the users identity info to the page if this is a user feed.
        """
        ctx = super(SquakList, self).get_context_data(**kwargs)
        if self.user:
            ctx['user'] = self.user
        return ctx

