# coding=utf-8

from django.utils import unittest
from goods.models import Stuff, Property


class StuffTestCase(unittest.TestCase):
    def test_unicode(self):
        stuff = Stuff(name=u'Стакан', description=u'Хороший стакан')
        self.assertEqual(u'Стакан (Хороший стакан)', unicode(stuff))


class PropertyTestCase(unittest.TestCase):
    def test_unicode(self):
        stuff = Stuff(name=u'Стакан', description=u'Хороший стакан')
        prop = Property(value=u'Хрустальный', stuff=stuff)
        self.assertEqual(u'Хрустальный - Стакан (Хороший стакан)', unicode(prop))
