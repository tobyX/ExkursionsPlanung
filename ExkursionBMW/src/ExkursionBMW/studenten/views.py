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
        s = Student.objects.filter(email__iexact=self.cleaned_data['email'])
        
	if not len(s) == 0:
	    s = s[0]
	    if s.vorname != self.cleaned_data['vorname'] or s.nachname != self.cleaned_data['nachname']:
                self._errors['email'] = self.error_class([u'Diese Email ist bereits für jemand anderen angemeldet?!'])
                if 'email' in self.cleaned_data:
                    del self.cleaned_data['email']
                return None

	return self.cleaned_data['email']

    def clean_exkurs1(self):

        if not self.cleaned_data['exkurs1'] or self.cleaned_data['exkurs1'] == 0:
            return None

        e = Exkursion.objects.filter(id=self.cleaned_data['exkurs1'], anzeige=1)

        if not len(e) == 1 or e[0].getTeilnehmerCount() >= e[0].maxTeilnehmer:
            self._errors['exkurs1'] = self.error_class([u'Falsche ID!'])
            if 'exkurs1' in self.cleaned_data:
                del self.cleaned_data['exkurs1']
        else:
            return self.cleaned_data['exkurs1']

    def clean_exkurs2(self):

        if not self.cleaned_data['exkurs2'] or self.cleaned_data['exkurs2'] == 0:
            return None

        e = Exkursion.objects.filter(id=self.cleaned_data['exkurs2'], anzeige=2)

        if not len(e) == 1 or e[0].getTeilnehmerCount() >= e[0].maxTeilnehmer:
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

	try:
            s = Student.objects.get(email__iexact=cleaned_data['email'], vorname__iexact=cleaned_data['vorname'], nachname__iexact=cleaned_data['nachname'])
        except Exception:
	    s = Student()

        s.vorname = cleaned_data['vorname']
        s.nachname = cleaned_data['nachname']
        s.email = cleaned_data['email']
        s.regtime = datetime.datetime.now()
        s.ip = request.META['REMOTE_ADDR']

        if cleaned_data['exkurs1']:
            s.exkurs1 = Exkursion.objects.get(id=cleaned_data['exkurs1'])
	else:
	    s.exkurs1 = None

        if cleaned_data['exkurs2']:
            s.exkurs2 = Exkursion.objects.get(id=cleaned_data['exkurs2'])
	else:
	    s.exkurs2 = None

        s.save()

        return HttpResponseRedirect('/liste/') # Redirect after POST

    def get_context(self, request, form):
        "Context for template rendering."
        return {'form': form,
                'exkursionen': self.exkursionen,
                'stage_field': self.unused_name('stage'),
                'state': self.state}
