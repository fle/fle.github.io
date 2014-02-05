My short drush cheat sheet
##############################

:date: 2011-01-31
:tags: drush
:category: development
:author: Florent Lebreton (fle)
:summary: Drush (DRUpal SHell) is a command-line which allows you to administer your Drupal site in console. It can be very useful when you have broken your site and when you can't access to your administration interface.

Drush (DRUpal SHell) is a command-line which allows you to administer your Drupal site in console.

It can be very useful when you have broken your site and when you can't access to your administration interface.


Drush command format:

.. code-block:: console

        $ drush [options] <command> [argument]


Below, a few basic commands offered by drush :

List all commands and get help:

.. code-block:: console

        $ drush
        $ drush help

Install Drupal ! (Very useful to deploy a dev instance quickly):

.. code-block:: console

        -- Download latest Drupal ...
        $ drush dl drupal
        -- or select a version ...
        $ drush dl drupal --select
        -- and install it !
        $ drush si --account-name=<USER> --account-pass=<PASS> --db-url=mysql://<DB_USER>:<DB_PASS>@localhost/<DB_NAME>

Clear Drupal caches (used 87 times today):

.. code-block:: console

        $ drush cc all

Install one or more module(s):

.. code-block:: console

        $ drush dl -y <MODULE> [<MODULE2>, ...]
        $ drush en -y <MODULE> [<MODULE2>, ...]

Disable and uninstall module(s):

.. code-block:: console

        $ drush dis -y <MODULE> [<MODULE2>, ...]
        $ drush pm-uninstall -y <MODULE> [<MODULE2>, ...]

Export database (intelligently, i.e. without cache tables and other stuff):

.. code-block:: console

        $ drush sql-dump --result-file=<DUMP_FILE.sql> --gzip

Launch Drupal cron:

.. code-block:: console

        $ drush cron

Update your Drupal site:

.. code-block:: console

        $ drush up

Of course, it's a very short list of basic drush commands, this post is just my drush newbie notes taken during `JulienD`_ presentation at #DCNantes. There is many other commands with drush core, some modules can extend this list and you can implement your own drush commands.

With some configuration, you can administer two sites or more easily.

.. _`JulienD`: http://twitter.com/juliendubreuil

