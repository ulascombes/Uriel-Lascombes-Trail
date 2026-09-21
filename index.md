---
layout: home
cover: /assets/images/courses/couverture.jpg
cover_position: "center 25%"
profile: /assets/images/portraits/profil.jpg
tagline: "Coureur de trail court"
---

{% assign p = site.data.profil %}
{% assign months = "janvier,février,mars,avril,mai,juin,juillet,août,septembre,octobre,novembre,décembre" | split: "," %}
{% assign timeline = site.data.resultats | concat: site.data.timeline | sort: "date" | reverse %}

<div class="timeline">
{% for item in timeline %}
  {% assign parts = item.date | date: "%Y-%m-%d" | split: "-" %}
  {% assign mnum = parts[1] | plus: 0 %}
  {% assign midx = mnum | minus: 1 %}
  {% assign jour = parts[2] | plus: 0 %}
  {% assign date_fr = jour | append: " " | append: months[midx] | append: " " | append: parts[0] %}

  {% if item.nom %}
  <div class="tl-item">
    {% if item.classement == 1 %}<span class="tl-medal gold">🏆</span>
    {% elsif item.classement == 2 %}<span class="tl-medal silver">🥈</span>
    {% elsif item.classement == 3 %}<span class="tl-medal bronze">🥉</span>
    {% else %}<span class="tl-dot"></span>
    {% endif %}
    <div class="tl-date">{{ date_fr }}</div>
    <div class="tl-title">
      {{ item.nom }}
      {% if item.classement == 1 %}<span class="tl-rank gold">1er</span>
      {% elsif item.classement == 2 %}<span class="tl-rank silver">2e</span>
      {% elsif item.classement == 3 %}<span class="tl-rank bronze">3e</span>
      {% elsif item.classement %}<span class="tl-rank">{{ item.classement }}e</span>
      {% endif %}
    </div>
    <div class="tl-meta">
      {% if item.km %}{{ item.km }} km{% endif %}
      {% if item.dplus %} · {{ item.dplus }} m D+{% endif %}
      {% if item.temps %} · {{ item.temps }}{% endif %}
    </div>
    {% if item.itra or item.utmb or item.betrail %}
    <div class="tl-scores">
      {% if item.itra %}<span class="tl-score-mini small">{% if p.itra_logo %}<img src="{{ p.itra_logo | relative_url }}" alt="ITRA">{% endif %}{{ item.itra }}</span>{% endif %}
      {% if item.utmb %}<span class="tl-score-mini small">{% if p.utmb_logo_general %}<img src="{{ p.utmb_logo_general | relative_url }}" alt="UTMB">{% endif %}{{ item.utmb }}</span>{% endif %}
      {% if item.betrail %}<span class="tl-score-mini small">{% if p.betrail_logo %}<img src="{{ p.betrail_logo | relative_url }}" alt="BeTrail">{% endif %}{{ item.betrail }}</span>{% endif %}
    </div>
    {% endif %}
  </div>
  {% else %}
  <div class="tl-item">
    <span class="tl-dot"></span>
    <div class="tl-date">{{ date_fr }}</div>
    {% if item.type %}<div class="tl-type">{{ item.type }}</div>{% endif %}
    <div class="tl-title">{{ item.titre }}</div>
    {% if item.description %}<div class="tl-desc">{{ item.description }}</div>{% endif %}
  </div>
  {% endif %}
{% endfor %}
</div>
