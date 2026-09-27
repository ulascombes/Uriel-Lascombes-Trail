# Site Uriel Lascombes

Site Jekyll servi par GitHub Pages à l'adresse
https://ulascombes.github.io/Uriel-Lascombes-Trail/

## Mise en ligne

1. Pousse le dépôt sur GitHub (`ulascombes/Uriel-Lascombes-Trail`).
2. Dans Settings > Pages : Source = « Deploy from a branch », branche `main`, dossier `/ (root)`.
3. Le site est en ligne en une à deux minutes.

Le `baseurl` de `_config.yml` doit correspondre au nom du dépôt. Si tu passes
sur un nom de domaine, mets le domaine dans `url` et vide `baseurl`.

## Ajouter une course

Ouvre `_data/resultats.yml` et copie un bloc en haut de la liste. Le tri,
les médailles (1er, 2e, 3e) et les chiffres de la saison sur l'accueil
se calculent tout seuls.

## Ajouter un récit de course

Crée `_recits/<ref>.md`, où `<ref>` est la même valeur que le champ `ref`
de la course dans `resultats.yml`. Le lien depuis la page Résultats
apparaît automatiquement. Modèle :

    ---
    title: "Nom de la course"
    ref: nom-course-2027
    date: 2027-04-10
    chapo: "Une ou deux phrases de résumé."
    image: /assets/images/photos/nom-course.jpg   # facultatif
    image_legende: "Nom de la course, avril 2027"
    ---

    Deux ou trois paragraphes.

    ## À retenir

    - Point 1
    - Point 2

Un récit qui contient `published: false` est un brouillon : il n'apparaît
pas sur le site (ni le lien « Récit » dans les résultats). Supprime cette
ligne quand il est prêt. Des brouillons existent déjà pour les courses
sans récit.

Les chiffres (place, distance, temps, cotes) et les chaussures sont repris
de `resultats.yml` : inutile de les répéter dans le récit.

## Tests de chaussures (plus tard)

La collection `_tests/` est déjà déclarée dans `_config.yml`. Il suffira
d'y créer un premier fichier `.md` et une page `tests.html` : le lien
« Tests » apparaîtra alors dans le menu.

## Crédits photos

Tout se passe dans `_data/photos.yml` :

1. déclare chaque photographe une seule fois dans `photographes` (nom + lien Instagram ou site) ;
2. dans `photos`, indique pour chaque fichier l'identifiant de son photographe.

Le crédit « Photo : Nom » s'affiche alors sous la photo, partout où elle est
utilisée, et le photographe est ajouté aux remerciements de la page À propos.
Le champ `cadrage` (ex. `"center 15%"`) permet de choisir la zone gardée
quand une photo est recadrée.

## Challenges

Les challenges sont décrits dans `_data/challenges.yml`. Pour rattacher une
course à un challenge, ajoute `challenges: [trails-provence]` à son bloc dans
`resultats.yml` : une étiquette avec le lien vers le site du challenge apparaît.

Un récit de bilan (par ex. celui du challenge en fin de saison) se crée comme
un récit normal dans `_recits/`, sans champ `ref`.

## Photos

Mets les photos en 1600 px de large maximum (2400 px pour la couverture)
dans `assets/images/photos/`. Les originaux de 10 Mo ralentissent le site.
Sur Mac : `sips -Z 1600 photo.jpg --out assets/images/photos/photo.jpg`.

## Cotes ITRA / UTMB / BeTrail

À mettre à jour à la main dans `_data/profil.yml` (cotes actuelles) et
dans `_data/resultats.yml` (cote de chaque course).

## Aperçu en local (facultatif)

    gem install bundler jekyll
    jekyll serve

puis ouvre http://localhost:4000/Uriel-Lascombes-Trail/
