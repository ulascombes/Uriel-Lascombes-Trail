# Uriel Lascombes – trail

Mon site perso : résultats, récits de course et chaussures testées.
En ligne sur https://ulascombes.github.io/Uriel-Lascombes-Trail/ (GitHub Pages, Jekyll).

## Où modifier quoi

| Je veux…                         | Fichier                                   |
|----------------------------------|-------------------------------------------|
| ajouter une course               | `_data/resultats.yml` (copier un bloc)    |
| écrire un récit                  | `_recits/<ref>.md`                        |
| ajouter une paire de chaussures  | `_tests/<nom>.md` + photo dans `assets/images/tests/` |
| mettre à jour mes cotes          | `_data/profil.yml`                        |
| créditer une photo               | `_data/photos.yml`                        |
| ajouter un article de presse     | `_data/presse.yml`                        |
| changer les objectifs            | `_data/objectifs.yml`                     |
| bilan d'une saison (leader, etc.)| `_data/saisons.yml`                       |
| texte de la page À propos        | `a-propos.html`                           |

Chaque fichier de `_data/` commence par quelques lignes qui expliquent ses champs.

## Récit

Le nom du fichier reprend le `ref` de la course dans `resultats.yml`, et le lien
« Récit de course » apparaît tout seul. Place, temps, distance et cotes viennent
de `resultats.yml`, pas besoin de les recopier.

    ---
    title: "Nom de la course"
    ref: nom-course-2027
    date: 2027-04-10
    chapo: "Une phrase de résumé."
    photos:
      - nom-course-2027-1.jpg
      - nom-course-2027-2.jpg
    ---

    Le récit.

    ## À retenir

    - …

Avec `published: false`, le récit reste en brouillon et n'apparaît pas sur le site.

## Photos

Dans `assets/images/photos/`, 1800 px de large maximum. Sur Mac :
`sips -Z 1800 photo.jpg --out assets/images/photos/photo.jpg`.
Les photos du haut de l'accueil (`hero_photos` dans `profil.yml`) existent aussi
en `-large.jpg` (2400 px) et `-small.jpg` (1200 px).

Si une photo est mal cadrée sur une carte, ajoute `cadrage: "center 20%"` à son
entrée dans `photos.yml` (0 % = on garde le haut, 100 % = le bas).

## Chaussures

Champs d'une fiche : `marque`, `title`, `nom_resultats` (le nom exact utilisé dans
le champ `chaussures` de `resultats.yml`), `taille`, `poids`, `drop`, `stack_talon`,
`stack_avant`, `image`. `podium: 1`, `2` ou `3` pour le podium, et
`sans_semelle: true` si le poids est pris sans la semelle de propreté.

## Aperçu en local

Depuis le dossier du site :

    docker run --rm -it -v "$PWD":/site -w /site -v jekyll-gems:/usr/local/bundle \
      -p 4000:4000 -p 35729:35729 ruby:3.3 \
      bash -c "gem install jekyll --no-document && jekyll serve --host 0.0.0.0 --livereload --force_polling"

puis http://localhost:4000/Uriel-Lascombes-Trail/. Après une modification de
`_config.yml`, il faut relancer la commande.

## Nom de domaine

Pour passer sur un domaine perso : le déclarer dans Settings > Pages, puis dans
`_config.yml` mettre le domaine dans `url` et vider `baseurl`.
