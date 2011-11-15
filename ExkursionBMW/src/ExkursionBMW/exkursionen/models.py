from django.db import models

class Exkursion(models.Model):
    bezeichnung = models.CharField(max_length=100)
    beschreibung = models.TextField()
    startzeit = models.DateTimeField()
    dauer = models.IntegerField()
    maxTeilnehmer = models.IntegerField()
    kosten = models.FloatField()
    anzeige = models.IntegerField()

    def __unicode__(self):
        return self.bezeichnung

    def getKostenProTeilnehmer(self):
        return self.kosten / self.maxTeilnehmer

    def getTeilnehmer(self):
        students = []

        if self.anzeige == 1:
            students += self.exkurs1.filter(exkurs1=self.id, exkurs2__isnull=False)
        if self.anzeige == 2:
            students += self.exkurs2.filter(exkurs2=self.id, exkurs1__isnull=False)

        return students

    def getTeilnehmerCount(self):
        students = []

        if self.anzeige == 1:
            students += self.exkurs1.filter(exkurs1=self.id, exkurs2__isnull=False)
        if self.anzeige == 2:
            students += self.exkurs2.filter(exkurs2=self.id, exkurs1__isnull=False)

        return len(students)

    def getWartende(self):
        students = []

        if self.anzeige == 1:
            students += self.exkurs1.filter(exkurs1=self.id, exkurs2__isnull=True)
        if self.anzeige == 2:
            students += self.exkurs2.filter(exkurs2=self.id, exkurs1__isnull=True)

        return students

    def getWartendeCount(self):
        students = []

        if self.anzeige == 1:
            students += self.exkurs1.filter(exkurs1=self.id, exkurs2__isnull=True)
        if self.anzeige == 2:
            students += self.exkurs2.filter(exkurs2=self.id, exkurs1__isnull=True)

        return len(students)
