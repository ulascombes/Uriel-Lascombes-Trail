---
layout: page
title: Résultats
permalink: /resultats/
---

{% assign p = site.data.profil %}
{% assign months = "janvier,février,mars,avril,mai,juin,juillet,août,septembre,octobre,novembre,décembre" | split: "," %}
{% assign courses = site.data.resultats | sort: "date" | reverse %}

<div class="timeline">
{% for c in courses %}
  {% assign parts = c.date | date: "%Y-%m-%d" | split: "-" %}
  {% assign mnum = parts[1] | plus: 0 %}
  {% assign midx = mnum | minus: 1 %}
  {% assign jour = parts[2] | plus: 0 %}
  {% assign date_fr = jour | append: " " | append: months[midx] | append: " " | append: parts[0] %}

  <div class="tl-item">
    {% if c.emoji %}<span class="tl-medal{% if c.classement == 1 %} gold{% elsif c.classement == 2 %} silver{% elsif c.classement == 3 %} bronze{% else %} neutral{% endif %}">{{ c.emoji }}</span>
    {% else %}<span class="tl-dot"></span>
    {% endif %}
    <div class="tl-date">{{ date_fr }}</div>
    <div class="tl-title">
      {{ c.nom }}
      {% if c.classement == 1 %}<span class="tl-rank gold">1er</span>
      {% elsif c.classement == 2 %}<span class="tl-rank silver">2e</span>
      {% elsif c.classement == 3 %}<span class="tl-rank bronze">3e</span>
      {% elsif c.classement %}<span class="tl-rank">{{ c.classement }}e</span>
      {% endif %}
    </div>
    <div class="tl-meta">
      {% if c.km %}{{ c.km }} km{% endif %}
      {% if c.dplus %} · {{ c.dplus }} m D+{% endif %}
      {% if c.temps %} · {{ c.temps }}{% endif %}
    </div>
    {% if c.commentaire %}<div class="tl-comment">« {{ c.commentaire }} »</div>{% endif %}
    {% if c.chaussures %}<div class="tl-shoes">Chaussures : {{ c.chaussures }}</div>{% endif %}
    {% if c.itra or c.utmb or c.betrail %}
    <div class="tl-scores">
      {% if c.itra %}<span class="tl-score-mini">{% if p.itra_logo %}<img src="{{ p.itra_logo | relative_url }}" alt="ITRA">{% endif %}{{ c.itra }}</span>{% endif %}
      {% if c.utmb %}<span class="tl-score-mini">{% if p.utmb_logo_general %}<img src="{{ p.utmb_logo_general | relative_url }}" alt="UTMB">{% endif %}{{ c.utmb }}</span>{% endif %}
      {% if c.betrail %}<span class="tl-score-mini">{% if p.betrail_logo %}<img src="{{ p.betrail_logo | relative_url }}" alt="BeTrail">{% endif %}{{ c.betrail }}</span>{% endif %}
    </div>
    {% endif %}
  </div>
{% endfor %}
</div>
