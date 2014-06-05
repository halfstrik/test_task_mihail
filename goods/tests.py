# coding=utf-8
from decimal import Decimal
from django.core.urlresolvers import reverse

from django.test import TestCase
from goods.models import Stuff, Property
from goods.views import get_stuff, get_properties


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
        stuff = Stuff.objects.create(name=u'Стакан', description=u'Хороший стакан', price=Decimal("10.0"))
        self.assertEqual([stuff], get_stuff(None, None))

    def test_get_stuff_with_two_stuff_item_but_requested_amount_one(self):
        stuff = Stuff.objects.create(name=u'Стакан1', description=u'Хороший стакан', price=Decimal("10.0"))
        Stuff.objects.create(name=u'Стакан2', description=u'Хороший стакан', price=Decimal("10.0"))
        self.assertEqual([stuff], get_stuff(1, None))

    def test_get_stuff_with_property_name(self):
        stuff = Stuff.objects.create(name=u'Стакан1', description=u'Хороший стакан', price=Decimal("10.0"))
        Property.objects.create(value=u'СуперСвойство', stuff=stuff)
        Stuff.objects.create(name=u'Стакан2', description=u'Хороший стакан', price=Decimal("10.0"))
        self.assertEqual([stuff], get_stuff(None, u'СуперСвойство'))

    def test_get_properties_when_no_properties(self):
        self.assertEqual([], get_properties())

    def test_get_properties_when_there_is_one_property(self):
        stuff = Stuff.objects.create(name=u'Стакан1', description=u'Хороший стакан', price=Decimal("10.0"))
        prop = Property.objects.create(value=u'TestProp', stuff=stuff)
        self.assertEqual([prop], get_properties())
