from django.db import models


class Stuff(models.Model):
    class Meta:
        db_table = u'stuffs'

    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.description)


class Property(models.Model):
    class Meta:
        db_table = u'properties'
        verbose_name_plural = u'properties'

    value = models.CharField(max_length=200)
    stuff = models.OneToOneField(Stuff)

    def __unicode__(self):
        return u'%s - %s' % (self.value, self.stuff)
