---
published: false
title: "Deux saisons face au même peloton"
date: 2026-11-22
etiquette: Analyse
chapo: "D'une course à l'autre, je recroise souvent les mêmes coureurs. Ils font un bon étalon pour mesurer ma progression, bien plus fiable que mes chronos."
image: /assets/images/photos/ventoux-2026-1.jpg
chiffres:
  - label: Temps sur un même parcours
    avant: "100"
    apres: "91,2"
    unite: "base 100"
  - label: Classement virtuel
    avant: "26e"
    apres: "3e"
    unite: "sur 626"
  - label: Équivalent cote UTMB
    avant: "712"
    apres: "781"
chiffres_note: "Fin 2024 – 2025 → second semestre 2026, face aux mêmes adversaires. Ce sont des estimations : la méthode est expliquée en fin d'article."
---

En trail, comparer deux chronos n'a pas beaucoup de sens : le parcours, le terrain et la météo changent tout. En revanche, sur les courses de la région, je recroise souvent les mêmes coureurs. Si je me rapproche d'eux, ou si je les distance davantage, c'est que j'ai progressé.

J'ai rassemblé les classements officiels de mes 18 courses depuis novembre 2024 : 6 394 classés au total, dont 625 coureurs que j'ai croisés au moins deux fois. Ce sont eux qui servent d'étalon. Aucun nom n'apparaît ici.

## Le principe

Chaque coureur a un niveau, chaque course une difficulté. Le temps d'un coureur, c'est en gros son niveau multiplié par la difficulté du jour. Comme des centaines de coureurs se croisent d'une course à l'autre, on peut estimer les deux à la fois.

Mon niveau est calculé séparément sur trois périodes : de fin 2024 à fin 2025, le premier semestre 2026, puis le second. J'ai écarté les Mélèzes, que j'ai fini en marchant à cause du genou.

## Ce qui a changé

<figure class="chart">
{% include graphiques/peloton-classement.svg %}
<figcaption>Chaque point est un coureur croisé au moins deux fois, placé selon son niveau estimé. Les traits verticaux marquent mon niveau sur chaque période.</figcaption>
</figure>

Face aux mêmes adversaires, je mets environ 8 % de temps en moins qu'en 2025. Sur une course de deux heures, ça représente une dizaine de minutes.

Fin 2025, 25 coureurs de ce groupe étaient estimés plus rapides que moi. En 2026, il n'en reste que trois, puis deux. Ces deux-là, je ne les ai croisés que deux fois, dont une aux championnats de France au Ventoux : leur niveau est beaucoup moins précis. Parmi les 184 coureurs croisés au moins trois fois, aucun n'est estimé plus rapide que moi depuis le début de l'année.

Le gros saut s'est fait entre fin 2025 et le printemps 2026. Depuis, la progression est plus lente : −8,2 % au premier semestre et −8,8 % au second, toujours par rapport à 2025. Ramené à l'échelle UTMB, ça donne 712, puis 775, puis 781. C'est un peu sous ma cote officielle actuelle (804), en partie à cause des championnats régionaux de novembre, qui tirent la moyenne vers le bas. La raison est juste en dessous.

## Plus ça grimpe, mieux ça va

<figure class="chart">
{% include graphiques/peloton-denivele.svg %}
<figcaption>Pour chaque course, l'écart entre ma performance du jour et mon niveau habituel, face aux mêmes adversaires. Les Mélèzes ne sont pas représentés.</figcaption>
</figure>

Course par course, ma performance dépend surtout du profil. Sur les parcours qui grimpent, au-delà de 55 m de dénivelé par kilomètre (Mimet, Volx, les Étoiles, le Col du Noyer), je suis 3 à 5 % plus rapide que d'habitude. Sur les parcours roulants, c'est l'inverse : 5,6 % plus lent aux Mineurs, 7,6 % aux championnats régionaux, avec seulement 23 m par kilomètre.

En moyenne, 10 m de dénivelé par kilomètre en plus, c'est environ 2,6 % de gagnés sur le peloton. Mon explication : sur le plat, beaucoup des coureurs que je croise vont presque aussi vite que moi, et l'écart ne se creuse vraiment que quand ça monte. Ça me donne une piste pour choisir mes courses.

## Le dernier tronçon

<figure class="chart chart-short">
{% include graphiques/peloton-troncons.svg %}
<figcaption>Mon rang sur chaque tronçon chronométré, comparé aux dix premiers de la course.</figcaption>
</figure>

Quand la course est serrée, je perds du temps sur la fin. Sur quatre des cinq courses dont les temps de passage sont publiés, mon dernier tronçon est mon moins bon.

Aux Mineurs, j'avais une minute d'avance au dernier pointage, et je termine deuxième à 8 secondes. Au Col du Noyer, j'étais deuxième sur les deux premiers tronçons, quatrième sur le dernier, et troisième à l'arrivée. Ce dernier tronçon, c'est souvent la descente finale, et mes autres données disent la même chose : la descente est mon point faible. Seule exception, Volx, où j'ai fait le meilleur temps sur chaque tronçon.

## La méthode, en bref

- Les données : les classements officiels de 18 courses, de novembre 2024 à novembre 2026. Seuls les coureurs croisés au moins deux fois servent à estimer les niveaux.
- Le modèle : le logarithme du temps est la somme du niveau du coureur et de la difficulté de la course, estimés ensemble sur tous les coureurs.
- L'équivalent UTMB est calé sur mes cotes de course officielles (11 courses).
- Les limites : un coureur croisé deux fois seulement est mal estimé, et le modèle ne tient compte ni du type de parcours ni de la forme du jour des autres. Ce sont des ordres de grandeur, pas des mesures.

## À retenir

- Face aux mêmes coureurs, je suis environ 8 % plus rapide qu'en 2025, surtout grâce au cap passé entre fin 2025 et le printemps 2026.
- Les parcours qui grimpent me réussissent nettement mieux que les roulants.
- La marge à aller chercher : le dernier tronçon, souvent en descente.
