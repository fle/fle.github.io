Easy Webmapping with django-leaflet & django-geojson
#####################################################

:date: 2014-06-29
:tags: django, webmapping, leaflet, geojson
:category: development
:slug: easy-webmapping-with-django-leaflet-and-django-geojson
:author: Florent Lebreton (fle)
:summary: Django-geojson is a set of tools to manipulate GeoJSON with Django. Django-leaflet allows you to use Leaflet in your Django projects. Together, they made webmapping really easy to play with.
:status: draft


Let's start with an important thing: I'm a real newbie in webmapping. I've never used Postgis, Mapnik, OpenLayers or <place any webmapping tool here>. Projection, SRID, ... are just some wild words for me.

For an estate management application, I wanted to place some markers on a map : a list of properties found after a search, the location of a consulted property, ... classic. As a Django developer, this application is written with my favorite framework!

`Mathieu <https://twitter.com/leplatrem>`_ told me about *django-geojson* and *django-leaflet*, two django apps he baked at Makina Corpus. Clearly, he didn't lie to me, **django-geojson and django-leaflet make webmapping really lightweight and friendly**. 

The magic thing is, since a few days, you really don't need a spatial database or some complex geographic libraries! Mathieu and I have removed the last dependencies to GEOS. I'm glad I could make this tiny contribution!

Django-geojson
--------------

`django-geojson <https://github.com/makinacorpus/django-geojson>`_ allows to manipulate GeoJSON (a JSON format for encoding geographic data structures) in a Django project. You can (de)serialialize objects and querysets, serve map layers through django views and store geographic data in JSON fields.

Django-leaflet
--------------

`django-leaflet <https://github.com/makinacorpus/django-leaflet>`_ provides a way to play with `Leaflet <http://leafletjs.com/>`_ very easily in a Django project. It embeds Leaflet assets, provides a form widget to edit geometries and a templatetag to display maps. In addition, it's highly configurable through django settings.

An Example
----------

Everybody loves mushrooms? Follow me, I'll show you some spots!

So I want to reference some mushroom spots, search for them and show them on a map. Here is the simple model which uses a ``PointField`` provided by ``django-geojson``:

.. code-block:: python

    # models.py
    from djgeojson.fields import PointField
    from django.db import models
    
    class MushroomSpot(models.Model):

        geom = PointField()

For the simplicity, when I create a mushroom spot instance, I want to point its location directly on a map. The admin widget coming with ``django-leaflet`` will help me:

.. code-block:: python

    # admin.py
    from leaflet.admin import LeafletGeoAdmin
    from django.contrib import admin

    admin.site.register(MushroomSpot, LeafletGeoAdmin)

The admin creation form looks like this and the widget allows me to place my marker easily:

.. image:: /images/012-admin-widget.png
    :alt: django-leaflet admin widget

For information - and I think it's crazy you don't even have to know this to make it all work! -, here is the JSON structure stored in database:

.. code-block:: javascript

    {
      "type":"Point",
      "coordinates":[
        -1.4058208465576172,
        47.15301133231325
      ]
    }

Edition is easy, now you'll see that display is too. To display a map, I use templatetags and filters provided by the two modules:

- ``leaflet_js`` and ``leaflet_css`` loads my Leaflet assets
- ``geojsonfeature`` helps me to serialize my MushroomSpot instances in a GeoJSON structure
- ``leaflet_map`` shows up the map!

My first view aims to show search results, stored in a queryset named ``qs_results``:

.. code-block:: django

    # mushroomspot_list.html
    {% extends "base.html" %}
    {% load leaflet_tags %}
    {% load geojson_tags %}

    {% block extra_assets %}
      {% leaflet_js %}
      {% leaflet_css %}
    {% endblock %}

    {% block content %}

        <script type="text/javascript">
          var collection = {{ qs_results|geojsonfeature|safe }};
          function map_init(map, options) {
              L.geoJson(collection).addTo(map);
          }
        </script>
        
        {% leaflet_map "spots" callback="window.map_init" %}

    {% endblock %}

The simple code above gives me something like this:

.. image:: /images/012-object-list.png
    :alt: simple map with django-leaflet and django-geosjson

Django-geojson can serialize a queryset, but it can also serialize a simple model instance. So for the detail view of a mushroom spot, code is almost the same, excepted the variable name of my data:

.. code-block:: django

    var collection = {{ mushroom_spot|geojsonfeature|safe }};

A little more
-------------

A great option of django-geojson allows to automatically serialize instance properties in the standard GeoJSON feature dictionnary ``properties``. Let's use it to add a pop-up on the marker!

I slightly adapt my model to add a description and a photo, which will be parts of my popup content. I also a write a property ``popupContent`` whose content will be serialized in the GeoJSON structure:

.. code-block:: python

    # models.py
    from djgeojson.fields import PointField
    from django.db import models
    
    class MushroomSpot(models.Model):

        geom = PointField()
        description = models.TextField()
        picture = models.ImageField()

        @property
        def popupContent(self):
          return '<img src="{}" /><p><{}</p>'.format(
              self.photo.url,
              self.description)

I've just to change the call of ``geojsonfeature``  alittle to specify properties I want to serialize and - for this particular use case - to use the Leaflet option ``onEachFeature``:

.. code-block:: django

        <script type="text/javascript">
          var collection = {{ mushroom_spot|geojsonfeature:"popupContent"|safe }};

          function onEachFeature(feature, layer) {
            if (feature.properties && feature.properties.popupContent) {
              layer.bindPopup(feature.properties.popupContent);
            }
          }

          function map_init(map, options) {
            L.geoJson(collection, {onEachFeature: onEachFeature}).addTo(map);
          }
        </script>

.. image:: /images/012-popup.png
    :alt: markers with popup thanks to django-geojson and django-leaflet

And that's it!


What's next?
------------

* My nexts tests will be to play with more complex geometries like lines or polygons. Django-geojson provides more fields than PointField like MultiPointField, PolygonField, ...
* For my estate management application, filling may be more simple if the marker was  automatically positioned after that the user has wrote the address. I think I could use `GeoPy <http://geopy.readthedocs.org/>`_ for this.
* An other solution would be to integrate `Leaflet GeoSearch plugin <https://github.com/smeijer/L.GeoSearch>`_ to the django-leaflet admin widget.


See you!
--------

If you have some observations or questions about this post, please leave a comment below.

Let's keep in touch on `twitter <http://twitter.com/__fle__>`_ or through this `blog feed </feeds/all.atom.xml>`_!

