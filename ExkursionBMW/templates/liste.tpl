{% extends "index.tpl" %}

{% block title %}Liste{% endblock %}

{% block content %}

{% if exkurse %}
    {% for ex in exkurse %}

        <h1>{{ ex.bezeichnung }}</h1>
        <h3>Teilnehmer {{ ex.getTeilnehmerCount }}</h3>
        <ul>
        {% for teilnehmer in ex.getTeilnehmer %}
            <li>{{ teilnehmer.nachname }}, {{ teilnehmer.vorname }} {% if teilnehmer.hatBezahlt %}&#x2714;{% endif %}</li>
        {% endfor %}
        </ul>
        <hr>
        <h3>Warteliste {{ ex.getWartendeCount }}</h3>
        <ul>
        {% for teilnehmer in ex.getWartende %}
            <li>{{ teilnehmer.nachname }}, {{ teilnehmer.vorname }}</li>
        {% endfor %}
        </ul>
        <br /> <br />
    {% endfor %}
{% endif %}

{% endblock %}