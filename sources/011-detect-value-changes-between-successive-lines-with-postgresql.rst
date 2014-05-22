Detect value changes between lines with PostgreSQL
##################################################

:date: 2014-05-21
:tags: postgresql
:category: development
:slug: detect-value-changes-between-successive-lines-with-postgresql
:author: Florent Lebreton (fle)
:summary: A window function performs a calculation across a set of rows that are related to the current row. Here is an example of utilisation of window functions lag and lead to detect value changes between successive table rows.

A few days ago, in a Django project, I had to solve a SQL problem that I had never met yet. Something like : "The last time that this column value has changed between a row and the next one". Crap...How?

By requesting help of `regilero <http://twitter.com/regilero>`_, who told me about **PostgreSQL window functions**.

Window Functions
----------------

To solve this, or any SQL query where you have to compare similar rows, PostgreSQL provides a usefull functionnality: `Window Functions <http://www.postgresql.org/docs/9.1/static/tutorial-window.html>`_. PostgreSQL 9.1.13 Documentation introduces this feature by saying:

    A window function performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result.

Different built-in window functions allows to compute rank of a row in a partition, get previous or next row value, etc. This kind of function must be invoked using window function syntax (i.e. with an ``OVER`` clause).

A simple example
----------------

Let's take a quite useless but simple example: 

- Each day, I take note on weather (How warm is it ? Is it rainy ?).
- I want to extract some information like:

  - On What day did the weather change?
  - When did it start to rain for the last time ?
  - ...

In a database, a very simple representation looks like this:

.. code-block:: console

    db=> \d weather
              Table « public.weather »
        Column      |  Type   | Modifiers 
        ------------+---------+---------------
        date        | date    | non NULL
        temperature | integer | non NULL
        rainy       | boolean | non NULL
 
and with sample data:

.. code-block:: console

    db=> SELECT * FROM weather ORDER BY date DESC;
        date       | temperature | rainy 
        -----------+-------------+-------
        2014-04-08 |          22 | f
        2014-04-07 |          20 | f
        2014-04-06 |          16 | t
        2014-04-05 |          18 | t
        2014-04-04 |          19 | t
        2014-04-03 |          22 | f
        2014-04-02 |          20 | f
        2014-04-01 |          18 | t

The very intersting part is here : thanks to window functions ``lag`` and ``lead``, I can **select for each row the column values of the previous and next rows**:

.. code-block:: sql

    SELECT
        date,
        rainy,
        lead(rainy) OVER (ORDER BY date DESC) as prev_rainy,
        lag(rainy) OVER (ORDER BY date DESC) as next_rainy
    FROM
        weather
    ORDER BY
        date DESC

.. code-block:: console

            date    | rainy | prev_rainy | next_rainy 
        ------------+-------+------------+------------
         2014-04-08 | f     | f          | 
         2014-04-07 | f     | t          | f
         2014-04-06 | t     | t          | f
         2014-04-05 | t     | t          | t
         2014-04-04 | t     | f          | t
         2014-04-03 | f     | f          | t
         2014-04-02 | f     | t          | f
         2014-04-01 | t     |            | f

Note: Obviously, the ORDER BY clause is very important here.

By nesting this in an other query, I can **detect value changes between rows** of my table. For example, the query below gives `"each day on which the weather changed"` (switch of the rainy boolean):

.. code-block:: sql

    SELECT
        w1.date, w1.rainy
    FROM
        (SELECT
            w2.date,
            w2.rainy,
            lead(w2.rainy) OVER (ORDER BY w2.date DESC) as prev_rainy
         FROM
            weather w2
         ORDER BY
            w2.date DESC) as w1
    WHERE
        w1.rainy IS DISTINCT FROM w1.prev_rainy
    ORDER BY
        w1.date DESC;

.. code-block:: console

            date   | rainy 
        -----------+-------
        2014-04-07 | f
        2014-04-04 | t
        2014-04-02 | f
        2014-04-01 | t

Based on this first selection, I can easily extract some other information like `"the last time the weather began to be nice"`:

.. code-block:: sql

    SELECT
        w1.date, w1.rainy
    FROM
        (SELECT
            w2.date,
            w2.rainy,
            lead(w2.rainy) OVER (ORDER BY w2.date DESC) as prev_rainy
         FROM
            weather w2
         ORDER BY
            w2.date DESC) as w1
    WHERE
        w1.rainy IS DISTINCT FROM w1.prev_rainy
    AND 
        w1.rainy IS FALSE
    ORDER BY
        w1.date DESC
    LIMIT 1;

.. code-block:: console

            date   | rainy 
        -----------+-------
        2014-04-07 | f


Go further
----------

Use case above is just an example focused on window functions lag and lead (I have no idea how to solve this kind of problem without them) but PostgreSQL provides other usefull `builtin window functions <http://www.postgresql.org/docs/9.1/static/functions-window.html#FUNCTIONS-WINDOW-TABLE>`_.

In addition, it's possible to call any built-in or user-defined aggregate function as a window function!


Stay tuned
----------

Keep in touch on `twitter <http://twitter.com/__fle__>`_, through this `blog feed </feeds/all.atom.xml>`_ or by commenting this article below!


[FR] Ce billet en français sur le blog de Makina Corpus : `Détecter un changement de valeurs entre deux lignes avec PostgreSQL <http://makina-corpus.com/blog/metier/2014/detecter-un-changement-de-valeurs-entre-deux-lignes-avec-postgresql>`_ !
