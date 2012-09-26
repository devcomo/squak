"""
Identity tests.
"""

from django.core.urlresolvers import reverse
from squak.apps.identity.test import IdentityTestBase
from squak.apps.identity.models import Identity


class EditIdentity(IdentityTestBase):
    """
    Test editing an identity.
    """
    def test_permissions(self):
        url = reverse('profile')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

        expected = '{0}?next=/identity/'.format(reverse('login'))

        self.assertRedirects(resp, expected)

    def test_edit(self):
        """
        Test editing a profile.
        """
        self.client.login(username=self.trane.username, password='pw')

        url = reverse('profile')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        data = {
            'name': self.trane.get_full_name(),
            'bio': 'Plays a little bit of saxophone',
            'email': 'trane@example.com',
        }

        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302)

        # the bio should have changed.
        identity = Identity.objects.get(user__username=self.trane.username)

        self.assertEqual(identity.bio, data['bio'])
