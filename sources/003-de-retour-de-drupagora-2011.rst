De retour de Drupagora 2011
###########################

:date: 2011-11-18
:tags: drupal
:category: geek stuff
:author: Florent Lebreton (fle)
:summary: Je reviens de la première édition de Drupagora, à Paris, qui se veut plus oriéntée chefs de projet/décideurs que les habituels DrupalCamps de geeks. Au final, une formule plutôt satisfaisante : Conférences intéressantes, beaucoup de retours d'expérience et un peu de technique quand même (ouf !).

Je reviens de la première édition de Drupagora, à Paris, qui se veut plus oriéntée chefs de projet/décideurs que les habituels DrupalCamps de geeks.
Au final, une formule plutôt satisfaisante : Conférences intéressantes, beaucoup de retours d'expérience et un peu de technique quand même (ouf !).


Mobilize, don't miniaturize
============================

Un premier constat de base
---------------------------

Le mobinaute :
* est boulimique d'information, très rapide, très volatile
* navigue avec une connexion lente et instable
* navigue sur un device peu performant

Il faut donc faire : léger, simple, concis, fontionnel


1. La mauvaise idée à la mode : une seule URL + Media Queries
--------------------------------------------------------------
Le responsive design n'est pas la panacée. L'idée est tentante, mais MediaQueries fait seulement de la réorganisation d'affichage, ce qui ne règle pas les problèmes d'ergonomie et de performances :
* le volume de données transféré est trop gros : DOM (surtout avec Drupal), images, js, css
* la consommation CPU est trop importante : scripts js et animations
* le contenu est trop long : articles trop longs, trop de blocs, ...

=> Cette solution est donc à réserver pour un site simple et léger (évenementiel par exemple)


2. Une solution plus aboutie : 2 URL + 2 themes
------------------------------------------------
* (MobileTools + Domains + DomainThemes + DomainAccess + DomainViews + Panels, TinySrc)
* Une URL de base pour le site sur ordinateur (rien de particulier à ce niveau)
* Une URL pour device mobile. Quelques recommandations pour le version mobile :

    Une des idées importantes est de profiter de la modernité des navigateurs mobiles (CSS3, HTML5, Storage) !!!

    Au niveau du thème

        * surcharger les .tpl pour alléger le DOM (DomainThemes)
        * penser au responsive design pour les différents devices (OmegaTheme ou AdaptiveTheme + PanelEverywhere + TinySrc)
        * éviter au maximum le javascript et la manipulation du DOM (consommation CPU importante) => Penser au CSS3, notamment à Translate3D (qui utilise le GPU et donc soulage le CPU).
        * pour les formulaires, l'audio, la vidéo, éviter là encore la javascript / Flash => Penser au HTML5
        * pour le js réellement nécessaire, se limiter à DOM Selector API ou jQuery Mobile
        * pour les sessions et le cache, éviter l'utilisation de cookies (transfert de data) =>  Penser au Session storage, Local storage, DB storage

    Au niveau du contenu

        * offrir la possibilité de publier une version résumée des articles (DomainAccess)
        * offrir la possibilité de publier une partie d'une page composite (variantes de Panel, Context, ...)

=> On a une version du site réellement adaptée au mobile avec :

    * Un contenu allégé, adapté au mode de lecture du mobinaute
    * Peu de HTML
    * Pas de JS
    * Beaucoup de cache navigateur


La gestion des 2 URLS nécessite:

    * Plan de redirection : il doit être implémenter au plus tôt dans l'architecture  (load-balancer -> proxy-cache -> apache -> Drupal si pas possible de faire autrement)
    * Détection de browser : Device detection => WURFL (plus OpenSource) vs. Browser detection => BrowserCap

    Attention à bien mettre en cache la redirection dans les headers HTTP pour ne pas la recalculer à chaque fois !


Exemple d'implémentation complète par Adyax : societegenerale.com

Les slides : http://www.drupagora.com/sites/default/files/slide/Drupal_et_Mobilite.pdf


Réussir son référencement et profiter de Drupal
================================================

Quelques trucs Google auxquels on ne pensent pas forcément
-----------------------------------------------------------
* "Être en 1ère page de Google n'a plus vraiment de sens" : Penser à se référencer sur "tous" les sites google : maps, youtube, shooping, ... selon le type de site
* Il est très largement préférable se positionner sur une multitude d'expressions qualifiées de 4/5/6 mots (longue traine), les expressions génériques sont inutiles
* Quand on fait des tests de référencement, attention à la personnalisation des résultats qui peut être trompeuse (cookies, géoloc, sites visités régulièrement, ...)


Évolutions des algorithmes Google en 2010-11-12-...
----------------------------------------------------
* Google Panda => Les pages à forte valeur ajoutée ont beaucoup plus d'importance que les aggrégateurs (news, comparateurs de prix, ...)
* Vers plus de "social ranking" => Facebook like, Google +1
* Arrivée du "person ranking" => La popularité de l'auteur de la page (Twitter, Facebook, Blog) va avoir une importance dans le positionnement de la page dans les prochains mois


La règle des 80/20 pour le référencement d'un site Drupal
----------------------------------------------------------
Avec Drupal, 80% de l'optimisation du référencement d'un site =  5 optimisations:

    1. Un bon title avec les bons mots-clés (en restant naturel : accents, majuscules, ...)
    2. Une bonne URL (sans paramètre, avec les bons mots-clés)
    3. Une bonne meta description pour attirer le clic (accroche du type "Livraison gratuite")
    4. Une bonne structure de site
    5. Une bonne structure sémantique HTML (h*, ul/li)
    6. (bonus) Avoir un title + H1 + URL indépendants les uns des autres !

Les autres 20% :

    Fil d'Ariane, taux de rebond (!!!), balises alternatives des images/vidéos, micro-formats, ...

Quelques modules Drupal
----------------------------------------------------
* URLs : PathAuto, PathAlias, PathRedirect, GlobalRedirect, Token
* Title : PageTitle, Taxonomy/Title
* Metas : Nodewords
* Sitemap : SitemapXML
* Linking interne : CKELink

Les slides : http://www.drupagora.com/sites/default/files/slide/presentation-Sebastien-Monnier-Woptimo-drupagora%20-%20V2.pptx


Gestion unifiée des medias chez Radio France
=============================================

RadioFrance est confronté au problème classique de la gestion des medias (sous D6 pour le moment) sur plusieurs sites. Leurs contraintes sont les suivantes :

    * Tout type de médias (photo, audio, video, flux externe, objets personnalisés)
    * Gestion de différents droits, licences, copyrights, expiration selon le media, la source, ...
    * Différents render de chaque media selon le context d'affichage (dans un wysiwyg ou non, sur device mobile, ...)
    * ~ 1.000.000 de nodes

L'implémentation technique est basée sur le module `Scald`_, initialement développé & utilisé par la radio publique de Chicago :

    * gère n'importe quel media
    * a son propre type de stockage unifiant (atoms) pour pallier à l'absence d'Entity sur D6
    * a sa propre gestion de cache
    * possède une gestion de "providers" pour pouvoir gérer des types de contenus media personnalisés !
    * D6 seulement, mais le portage D7 est prévu pour Q1 2012

La solution construite par RadioFrance consiste en une bibliothèque partagée qui liste tous les medias disponibles au contributeur (Scald + Views + Lightbox):

    * visible et accessible en permanence dans un bandeau droit vertical,
    * filtres ajax (titre, type de media, tags, licences, ...) + enregistrement de recherches personnalisées,
    * prévisualisation de n'importe quel media en lightbox
    * ajout d'un nouveau media lightbox (sans quitter le node en cours de création donc !)

L'intégration d'un media dans un contenu se fait par un simple Drag & Drop :

    * soit directement dans un WYSIWYG, avec le rendu final automatique. Exemple :

        * pour une photo : affichage de l'image + légende + copyright,
        * pour un audio ou une video : affichage du player thémé.

    * soit dans un fieldset du formulaire (stockage dans un field caché)

Ergonomiquement pour le contributeur ... c'est très sympa !

Pour le passage à D7, RadioFrance hésite entre Scald et Media :

    * Entity rend redondante la couche d'abstraction créée par Scald avec Atom
    * Pour le moment, l'interface et les fonctionnalités de Media sont plus basiques que Scald (integration Views inexistante ou très récente, gestion pauvre des licences/expiration, ...), mais il y a bien sûr la possibilité d'ajouter des plugins
    * Le développement de Media avance vite, et rattrape petit à petit Scald

    => Selon RadioFrance, impossible d'être influent sur l'orientation de Media face à Acquia, donc RadioFrance va choisir d'aider au portage de Scald sur D7 plutôt que de contribuer à Media ...

A tester aussi : le module `MediaFront`_ basé sur Media.

.. _Scald : http://drupal.org/project/scald
.. _MediaFront : http://drupal.org/project/mediafront

