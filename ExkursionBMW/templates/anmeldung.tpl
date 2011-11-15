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
<br />
<hr />
{% for id,exkurs in exkursionen.items %}
	<div class="checkboxes">
		{% if id == 1 %}
			{{ form.exkurs1.errors }}
		{% else %}
			{{ form.exkurs2.errors }}
		{% endif %}
    	{% for ex in exkurs %}
		<p class="checkbox">
        	<input type="radio" name="exkurs{{ id }}" value="{{ ex.id }}"
        	{% if ex.maxTeilnehmer <= ex.student_set.count %} disabled="disabled"{% endif %}
        	{% if form.exkurs1.data|slugify == ex.id|slugify or form.exkurs2.data|slugify == ex.id|slugify %} checked="checked"{% endif %} />
		<label for="exkurs{{id}}"><b>{{ ex.bezeichnung }}</b> <br />
			{% if ex.bezeichnung != 'Warteliste' %}
        		<b>Startzeit: {{ ex.startzeit }}</b><br />
        		Dauer: {{ ex.dauer }} Minuten<br />
        		Maximale/Aktuelle Teilnehmer: {{ ex.maxTeilnehmer }} / {{ ex.getTeilnehmerCount }}<br />
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

<input type="submit" value="Submit" />
</form>

{% endblock %}
