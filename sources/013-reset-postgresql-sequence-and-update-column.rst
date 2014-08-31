Reset a PostgreSQL sequence and update column values
#####################################################

:date: 2014-08-31
:tags: postgresql
:category: quick tips
:author: Florent Lebreton (fle)
:slug: reset-a-postgresql-sequence-and-recompute-column-values
:summary: A simple way to reset and restart a broken PostgreSQL sequence.

Yesterday, I understood that I had broken a sequence of an auto-increment column in my PostgreSQL database. This quick tip will show you how to reset the sequence, restart it to a specific value, and recreate all values of the column

Example
========

I have a table which stores estate properties. Each property is associated to list of pictures (gallery). A joint table does this association

.. code-block:: console

    db=> \d weather
              Table « public.property_pictures »
       Colonne   |  Type   |                           Modificateurs                           
    -------------+---------+-------------------------------------------------------------------
     id          | integer | non NULL default, nextval('property_gallery_id_seq'::regclass)
     property_id | integer | non NULL
     picture_id  | integer | non NULL

My ``property_gallery_id_seq`` sequence is dizzy and generates conflict on the ``id`` values.

Solution
=========

Here is a solution.

1. Set temporary values intentionally far of existing values to avoid conflicts when we recompute the column:


.. code-block:: sql

    UPDATE property_pictures SET id=10000+nextval('property_gallery_id_seq');
    

2. Restart sequence to 1


.. code-block:: sql

    ALTER SEQUENCE property_gallery_id_seq RESTART WITH 1;


3. Rewrite all column values


.. code-block:: sql

    UPDATE property_pictures SET id=nextval('property_gallery_id_seq');


Note: Obviously, be very careful if the column is used a foreign key ... Also, do not forget to search WHY your sequence has been broken anyway ...

This solution is strongly inspired by this `stackoverflow post <http://stackoverflow.com/questions/4678110/how-to-reset-sequence-in-postgres-and-fill-id-column-with-new-data>`_

I hope this trick can save you some time too!

`__fle__ <http://twitter.com/__fle__>`_