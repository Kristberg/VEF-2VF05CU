{% extends "base.html" %}

{% block title %}Bensinstöðvar{% endblock %}
{% block content %}
<table>
    <tr>
        <th>Fyrirtæki</th><th>Staður</th>
    </tr>

    {% set cnt = [] %}
    {% for item in gogn['results'] %}
    <tr>
        {% if item.company == com %}
        {% do cnt.append(item.company) %}
        <td><a href="/moreinfo/{{item.key}}">{{item.company}}</a></td>
        <td>{{item.name}}</td></tr>
        {% endif %}
    {% endfor %}
</table>
    <h3>Fjöldi stöðva:{{ cnt | length }}</h3>
{% endblock %}