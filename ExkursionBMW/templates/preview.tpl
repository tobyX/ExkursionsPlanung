{% extends "index.tpl" %}

{% block title %}Preview{% endblock %}

{% block content %}

<h1>Überprüfen Sie Ihre Daten</h1>

<div class="preview">
    <label for="formtools_vorname">Vorname:</label>
    {{ form.vorname.data }}
</div>
<div class="preview">
    <label for="formtools_nachname">Nachname:</label>
    {{ form.nachname.data }}
</div>
<div class="preview">
    <label for="formtools_email">Email-Adresse:</label>
    {{ form.email.data }}
</div>
<br />
{% for id,exkurs in exkursionen.items %}
	<div class="fieldWrapper">
    	{% for ex in exkurs %}
    		{% if form.exkurs1.data|slugify == ex.id|slugify or form.exkurs2.data|slugify == ex.id|slugify %}
        		<b>{{ ex.bezeichnung }}</b> <br />
			{% if ex.bezeichnung != 'Warteliste' %}
        		<b>Startzeit: {{ ex.startzeit }}</b><br />
        		Dauer: {{ ex.dauer }} Minuten<br />
        		Maximale/Aktuelle Teilnehmer: {{ ex.maxTeilnehmer }} / {{ ex.getTeilnehmerCount }}<br />
        		Beschreibung: <br />
        		{{ ex.beschreibung }}
			{% endif %}
        	{% endif %}
    	{% endfor %}
    </div>
    {% if not forloop.last %}
	<hr>
	{% endif %}
{% endfor %}

<form action="" method="post">{% csrf_token %}
{% for field in form %}{{ field.as_hidden }}
{% endfor %}
<input type="hidden" name="{{ stage_field }}" value="2" />
<input type="hidden" name="{{ hash_field }}" value="{{ hash_value }}" />
<p><input type="submit" value="Submit" /></p>
</form>

{% endblock %}
