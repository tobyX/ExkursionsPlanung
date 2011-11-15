# coding=UTF8

from studenten.models import Student
from exkursionen.models import Exkursion
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django import forms
import datetime
from django.contrib.formtools.preview import FormPreview

class AnmeldeForm(forms.Form):
    vorname = forms.CharField(max_length=255)
    nachname = forms.CharField(max_length=255)
    email = forms.EmailField()
    exkurs1 = forms.IntegerField(required=False)
    exkurs2 = forms.IntegerField(required=False)

    def clean_email(self):
        s = Student.objects.filter(email__istartswith=self.cleaned_data['email'])

        if not len(s) == 0:
            self._errors['email'] = self.error_class([u'Diese Email ist bereits angemeldet, für Änderungen bitte Mail an fom@tobyf.de'])
            if 'email' in self.cleaned_data:
                del self.cleaned_data['email']
        else:
            return self.cleaned_data['email']

    def clean_exkurs1(self):

        if not self.cleaned_data['exkurs1']:
            return None

        e = Exkursion.objects.filter(id=self.cleaned_data['exkurs1'], anzeige=1)

        if not len(e) == 1:
            self._errors['exkurs1'] = self.error_class([u'Falsche ID!'])
            if 'exkurs1' in self.cleaned_data:
                del self.cleaned_data['exkurs1']
        else:
            return self.cleaned_data['exkurs1']

    def clean_exkurs2(self):

        if not self.cleaned_data['exkurs2']:
            return None

        e = Exkursion.objects.filter(id=self.cleaned_data['exkurs2'], anzeige=2)

        if not len(e) == 1:
            self._errors['exkurs2'] = self.error_class([u'Falsche ID!'])
            if 'exkurs2' in self.cleaned_data:
                del self.cleaned_data['exkurs2']
        else:
            return self.cleaned_data['exkurs2']

class AnmeldeFormPreview(FormPreview):

    form_template = 'anmeldung.tpl'
    preview_template = 'preview.tpl'

    ex_objs = Exkursion.objects.all()

    exkursionen = {}
    for ex in ex_objs:
        if not exkursionen.has_key(ex.anzeige):
            exkursionen[ex.anzeige] = []
        exkursionen[ex.anzeige].append(ex)

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.

        s = Student()
        s.vorname = cleaned_data['vorname']
        s.nachname = cleaned_data['nachname']
        s.email = cleaned_data['email']
        s.regtime = datetime.datetime.now()
        s.ip = request.META['REMOTE_ADDR']

        if cleaned_data['exkurs1']:
            s.exkurs1 = Exkursion.objects.get(id=cleaned_data['exkurs1'])

        if cleaned_data['exkurs2']:
            s.exkurs2 = Exkursion.objects.get(id=cleaned_data['exkurs2'])

        s.save()

        return HttpResponseRedirect('/liste/') # Redirect after POST

    def get_context(self, request, form):
        "Context for template rendering."
        return {'form': form,
                'exkursionen': self.exkursionen,
                'stage_field': self.unused_name('stage'),
                'state': self.state}
