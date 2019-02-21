{% extends 'base.html' %}
{% block title %}Nánari upplýsingar bensínstöðvar{% endblock %}
{% block content %}
    <h2>Nánari upplýsingar bensínstöðvar</h2>
    {% for item in gogn['results'] %}
        {% if item.key == k %}
            <h3>Söluaðili: {{item.company}}</h3>
            <h3>Staður: {{item.name}}</h3>
            <h3>Verð á 1 líter af Bensíni, 95 oktan: {{item.bensin95}} kr</h3>
            <h3>Verð á 1 líter af Dísel olíu: {{item.diesel}} kr</h3>
        <div class="kort">
            <h4>Staðsetning bensínstöðvar</h4>
            <ul>
                <li>Breiddargráða: {{item.geo.lat}}</li>
                <li>Lengdargráða: {{item.geo.lon}}</li>
                <li><a href="https://www.google.com/maps/@{{item.geo.lat}},{{item.geo.lon}},18z/">Staðsetning á google maps</a></li>
            </ul>
        {% endif %}
    {% endfor %}
{% endblock %}