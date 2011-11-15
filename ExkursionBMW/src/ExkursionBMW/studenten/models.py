from django.db import models
from django.db.models import Q

# Create your models here.
class Student(models.Model):
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    ip = models.IPAddressField()
    regtime = models.DateTimeField()
    exkurs1 = models.ForeignKey('exkursionen.Exkursion', related_name='exkurs1', limit_choices_to = {'anzeige': 1}, blank=True, null=True)
    exkurs2 = models.ForeignKey('exkursionen.Exkursion', related_name='exkurs2', limit_choices_to = {'anzeige': 2}, blank=True, null=True)

    def __unicode__(self):
        return self.vorname + ' ' + self.nachname
