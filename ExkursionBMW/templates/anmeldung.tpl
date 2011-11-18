{% extends "index.tpl" %}

{% block title %}Anmeldung{% endblock %}

{% block content %}

<form action="" method="post">
{% csrf_token %}

<input type="hidden" name="{{ stage_field }}" value="1" />
	{{ form.non_field_errors }}
    <div class="fieldWrapper">
        {{ form.vorname.errors }}
        <label for="formtools_vorname">Vorname:</label>
        {{ form.vorname }}
    </div>
    <div class="fieldWrapper">
        {{ form.nachname.errors }}
        <label for="formtools_nachname">Nachname:</label>
        {{ form.nachname }}
    </div>
    <div class="fieldWrapper">
        {{ form.email.errors }}
        <label for="formtools_email">Email-Adresse:</label>
        {{ form.email }}
    </div>
    <p style="font-size: 0.8em">Zum Ändern (auch Löschen) einer Eintragung die Anmeldung mit den gleichen Daten nochmals durchführen!</p>
<br />
<hr />
{% for id,exkurs in exkursionen.items %}
	<h2>{{ id }}. Exkursion</h2>
	<div class="checkboxes">
		{% if id == 1 %}
			{{ form.exkurs1.errors }}
		{% else %}
			{{ form.exkurs2.errors }}
		{% endif %}

		<p class="checkbox">
			<input type="radio" name="exkurs{{ id }}" value="0"
			{% if id == 1 %}
			{% if not form.exkurs1.data or form.exkurs1.data == "0" %} checked="checked"{% endif %}
			{% else %}
			{% if not form.exkurs2.data or form.exkurs2.data == "0" %} checked="checked"{% endif %}
			{% endif %}/>
			<label for="exkurs{{ id }}"><b>Keine Teilnahme</b></label>
		</p>

    	{% for ex in exkurs %}
		<p class="checkbox">
        	<input type="radio" name="exkurs{{ id }}" value="{{ ex.id }}"
        	{% if ex.maxTeilnehmer <= ex.getTeilnehmerCount %} disabled="disabled"{% endif %}
        	{% if form.exkurs1.data|slugify == ex.id|slugify or form.exkurs2.data|slugify == ex.id|slugify %} checked="checked"{% endif %} />
			<label for="exkurs{{ id }}"><b>{{ ex.bezeichnung }}</b> <br />
			{% if ex.bezeichnung != 'Warteliste' %}
        		<b>Startzeit: {{ ex.startzeit }}</b><br />
        		Dauer: {{ ex.dauer }} Minuten<br />
        		Maximale/Aktuelle Teilnehmer: {{ ex.maxTeilnehmer }} / {{ ex.getTeilnehmerCount }}<br />
				Kosten pro Teilnehmer: {{ ex.getKostenProTeilnehmer|floatformat:"2" }} Euro<br />
        		Beschreibung: <br />
        		{{ ex.beschreibung }}
			{% endif %}
		</label>
		</p>
    	{% endfor %}
    </div>

	{% if not forloop.last %}
	<hr>
	{% endif %}

{% endfor %}

<br />
<p>Bitte beachten: Wer nur an einer Exkursion teilnimmt, landet vorerst nur auf einer Warteliste!</p>
<p>Der Eintrittspreis wird vorab von uns (<a href="mailto: &#102;&#108;&#111;&#114;&#105;&#97;&#110;&#46;&#109;&#97;&#114;&#113;&#117;&#97;&#114;&#100;&#64;&#103;&#111;&#111;&#103;&#108;&#101;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;">Flo</a>, <a href="mailto: &#102;&#111;&#109;&#64;&#116;&#111;&#98;&#121;&#102;&#46;&#100;&#101;">Toby</a>) eingesammelt,
wer dann trotzdem nicht kommt hat keinen Anspruch auf Rückvergütung, es sei denn es rückt eine andere Person nach.</p>

<input type="submit" value="Submit" />
</form>

{% endblock %}
