Combine LDAP and classical authentication in django 
####################################################

:date: 2013-12-20
:tags: django, ldap
:category: python
:author: Florent Lebreton (fle)
:status: draft

Still in our CAMM project `JOB <http://makina-corpus.com/realisations/application-de-gmao>`_ at `Makina Corpus <http://makina-corpus.com>`_, we needed to provide an authentication through a LDAP server. The module `django-auth-ldap <http://https://pypi.python.org/pypi/django-auth-ldap>`_ does most of work itself but ... We decided to combine this LDAP authentication with the classical django authentication for two reasons:

* Allow user creations in the django database without having them in the LDAP directory (mainly `superusers`);
* Be able to fallback on django authentication for all users in case of a LDAP server failure.

So to handle this, we have to:

* Differentiate users coming from LDAP directory from users existing only in django;
* Store password of LDAP users in django to be able to switch on classical authentication;
* Implement two custom authentication backends;




