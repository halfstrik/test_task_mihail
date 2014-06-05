# coding=utf-8
from django.core.urlresolvers import reverse

from django.test import TestCase
from goods.models import Stuff, Property
from goods.views import get_stuff


class StuffTestCase(TestCase):
    def test_unicode(self):
        stuff = Stuff(name=u'Стакан', description=u'Хороший стакан')
        self.assertEqual(u'Стакан (Хороший стакан)', unicode(stuff))


class PropertyTestCase(TestCase):
    def test_unicode(self):
        stuff = Stuff(name=u'Стакан', description=u'Хороший стакан')
        prop = Property(value=u'Хрустальный', stuff=stuff)
        self.assertEqual(u'Хрустальный - Стакан (Хороший стакан)', unicode(prop))


class StuffViewTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse(u'home'))
        self.assertEqual(response.status_code, 200)

    def test_get_stuff_without_stuff(self):
        self.assertEqual([], get_stuff(None, None))

    def test_get_stuff_with_one_stuff_item(self):
        stuff = Stuff.objects.create(name=u'Стакан', description=u'Хороший стакан')
        self.assertEqual([stuff], get_stuff(None, None))

    def test_get_stuff_with_two_stuff_item_but_requested_amount_one(self):
        stuff = Stuff.objects.create(name=u'Стакан1', description=u'Хороший стакан')
        Stuff.objects.create(name=u'Стакан2', description=u'Хороший стакан')
        self.assertEqual([stuff], get_stuff(1, None))
