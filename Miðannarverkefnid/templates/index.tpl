{% extends "base.html" %}
{% block title%}Eldsneytisverð - miðannarverkefni - json{% endblock %}
{% block content %}
<p> Fyrirtækin birtast aftur einu sinni á forsíðu </p>
<div class="wrapper">
    {% set one = [] %}
    {% for item in gogn['results'] %}
        {% if item.company not in one %}
            {% do one.append(item.company) %}
            <div class="box"><a href="/company/{{ item.company}}">{{item.company}}</a></div>
        {% endif %}
    {% endfor %}
    <div class="kort">
        <h2>Besta Verðið</h2>
        <h4>Ódýrasta bensínið: <i>{{minpriceP}} kr.</i> er hjá {{companyP}}</h4>
        <h4>Ódýrasta diesel olían: <i>{{minpriceD}} kr.</i> er hjá {{companyD}}</h4>
        <p>Síðast uppfært: {{gogn.timestampPriceCheck }}</p>
    </div>
</div>
{% endblock %}
