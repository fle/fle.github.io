Temporarily disable all indexes of a postgresql table
#####################################################

:date: 2018-04-10
:tags: postgresql
:category: quick tips
:author: Florent Lebreton (fle)
:slug: temporarily-disable-all-indexes-of-a-postgresql-table
:summary: Disable temporarily and reenable table indexes can be useful to speed up a large insert or update query

When you run a large query (insert/update) on a huge table with several indexes, these indexes can seriously slow the query execution.

With Postgresql it can be very faster to disable the indexes before runing the query and reindex all the table afterwards.

You can do it like this :


1. Disable all table indexes


.. code-block:: sql

    UPDATE pg_index 
    SET indisready=false
    WHERE indrelid = (
        SELECT oid
        FROM pg_class
        WHERE relname='<TABLE_NAME>'
    );


2. Run your query


.. code-block:: sql

    UPDATE <TABLE_NAME> SET ...;


3. Reenable all table indexes


.. code-block:: sql

    UPDATE pg_index 
    SET indisready=true
    WHERE indrelid = (
        SELECT oid
        FROM pg_class
        WHERE relname='<TABLE_NAME>'
    );


4. Reindex table


.. code-block:: sql

    REINDEX <TABLE_NAME>;


I saved some time with this trick so I just wanted to share it!

`__fle__ <http://twitter.com/__fle__>`_