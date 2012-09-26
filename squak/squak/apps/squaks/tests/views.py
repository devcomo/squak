"""
Squak tests.
"""

from django.core.urlresolvers import reverse
from squak.apps.identity.test import IdentityTestBase
from squak.apps.squaks.models import Squak


class CreateSquak(IdentityTestBase):
    """
    Tests about creating squaks
    """
    def test_permissions(self):
        """
        ensure a user who is logged out doesn't see the form.
        """
        url = reverse('create-squak')

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)

        expected = '{0}?next=/create/'.format(reverse('login'))

        self.assertRedirects(resp, expected)

    def test_create_squak(self):
        """
        Test creating a squak
        """
        self.client.login(username=self.miles.username, password='pw')

        miles_squak_count = Squak.objects.filter(owner=self.miles).count()

        url = reverse('create-squak')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        data = {
            'text': 'this is my new squak. You dig?'
        }

        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 302)

        self.assertEqual(Squak.objects.filter(owner=self.miles).count(),
            miles_squak_count + 1)
