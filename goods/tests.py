# coding=utf-8
from django.core.urlresolvers import reverse

from django.test import TestCase
from goods.models import Stuff, Property
from goods.views import StuffIndexView


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
    def test_StuffIndexView_get_queryset_when_there_is_no_stuff(self):
        self.assertEqual(list(StuffIndexView().get_queryset()), [])

    def test_StuffIndexView_get_queryset_when_there_is_one_stuff(self):
        stuff = Stuff.objects.create(name=u'Стакан', description=u'Хороший стакан')
        self.assertEqual(list(StuffIndexView().get_queryset()), [stuff, ])

    def test_stuff_index_view_when_one_stuff_present(self):
        Stuff.objects.create(name=u'Стакан', description=u'Хороший стакан')
        response = self.client.get(reverse(u'goods:stuff_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Стакан')
        self.assertQuerysetEqual(response.context[u'stuffs'], ['<Stuff: Стакан (Хороший стакан)>'])
