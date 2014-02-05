Capturez une signature manuscrite avec django-jsignature
#########################################################

:date: 2013-11-27
:tags: django, jsignature
:category: development
:author: Florent Lebreton (fle)
:summary: Comment capturer une signature "électronique-manuscrite" dans Django avec l'application django-jsignature et le plugin javascript jSignature.


Aujourd'hui, tous les documents (ou presque) générés par l'activité d'une entreprise sont créés informatiquement.
Dans certains cas, l'impression d'un document est nécessaire uniquement pour apposer une signature (de l'envoyeur, du destinataire, ou autre).

Dans le cadre d'un projet de `GMAO full web <http://makina-corpus.com/realisations/application-de-gmao>`_ chez `Makina <http://makina-corpus.com>`_, nous avons mis en place, pour les techniciens itinérants, un formulaire de saisie de rapport signé sur tablette tactile.

Ce process, réalisé sur place et immédiatement après l'intervention, permet un gain de temps important en évitant les doubles saisies, les impressions et les échanges mails et courriers.

Bien que la signature "électronique-manuscrite" n'est pas une preuve totalement valable aux yeux de la loi, pouvoir apposer une signature via une tablette tactile peut être vraiment utile et éviter des impressions et des échanges inutiles :).

La fonctionnalité de signature a été réalisée avec jSignature, wrappée dans une app django.

jSignature et django-jsignature
--------------------------------

`jSignature <https://github.com/brinley/jSignature/blob/master/README.md>`_ est un plugin jQuery qui transforme un simple <div> en cadre prêt à recevoir une signature déssinée à la souris ou mieux, sur écran tactile. Quelques options de configuration sont disponibles et l'export de la signature est possible dans différents formats (image base/64, image base/30, json, ...).

Nous avons publié `django-jsignature <https://github.com/fle/django-jsignature>`_, une petite app django permettant :

* d'avoir facilement un champ "signature" dans un formulaire django (avec un field et un widget);
* de faire le rendu de l'image en python (avec Pillow);
* de stocker la signature (json) et la date de signature dans un modèle (champs fournis par un mixin);

Le billet complet est sur le `blog de Makina <http://makina-corpus.com/blog/metier/signez-vos-documents-sur-tablette-tactile-avec-django-jsignature>`_.

Le code est dispo sur `github <https://github.com/fle/django-jsignature.git>`_.
