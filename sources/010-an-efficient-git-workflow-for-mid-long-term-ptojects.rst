An efficient GIT workflow for mid/long term projects
####################################################

:date: 2014-02-12
:tags: git
:category: development
:author: Florent Lebreton (fle)

Our `full-web CAMM project <http://makina-corpus.com/realisations/application-de-gmao>`_
at `Makina Corpus <http://makina-corpus.com>`_ has been going on for nearly two
years and is running in production for over 18 months. I think it's my first project
without any headache about our codebase and VCS management. So, I'll present our
GIT workflow which has proven to be very effective for now.

Context
--------

* Several developers
* Several staging/pre-production servers, several (non-synchronous) production servers
* Monthly releases (more or less) with delivery on staging, then on production servers
* On servers, basecode is directly pulled from the GIT repository with fabric

Rules
------

To handle this, we have set some simple rules:

.. raw:: html

	<div class="box center only-list">


1. One (and only one) maintainer, who manage GIT repository and releases
2. Never commit directly on ``master``
3. Never rebase ``master`` on any branch
4. Do not get out of planned workflow


.. raw:: html

	</div>

Workflow
---------

Master branch
++++++++++++++

Our branch ``master`` is the common trunk and simply contains all the codebase of
the next release. Since we don't work directly on it, it evolves mainly with merges.


.. image:: /images/010-gw1.png
    :alt: Workflow GIT 1

Development branches
+++++++++++++++++++++

When a developer starts a new feature or a bugfix, he creates a new branch from
``master`` ``HEAD``

.. code-block:: console

	$ (master) git checkout -b featureA
	$ (featureA) git commit -a -m "featureA part 1"
	$ (featureA) git commit -a -m "featureA part 2"


.. image:: /images/010-gw2.png
    :alt: Workflow GIT 2

He follows branch ``master`` evolution and regularly ensures his code still works,
by rebasing his branch ``featureA`` on branch ``master``.

.. code-block:: console

	$ (featureA) git rebase master

When his developments are done (commits *fa1* / *fa2* in schema below), he does a last rebase. Thanks to this:

* he ensures that the maintainer will be able to merge easily (maintainer should not need to read code deeply and search why there are conflicts)
* if tests pass on development branch after rebase, they should pass on ``master`` after merge, so **we ensure that branch ``master`` is always working well**

Possibly, it will be the good time to
`clean the development branch <http://fle.github.io/git-tip-keep-your-branch-clean-with-fixup-and-autosquash.html>`_
to let it neat just when it is finished.

.. image:: /images/010-gw3.png
    :alt: Workflow GIT 3

The maintainer can now merge this branch in ``master`` peacefully, without big
conflict troubles. As the maintainer, I like to use ``no-ff`` option to force a 
*merge commit*, so **history can stay really readable** (we easily see where the
branch has started and where it has been merged).

.. code-block:: console

	$ (master) git merge --no-ff featureA


.. image:: /images/010-gw4.png
    :alt: Workflow GIT 4

Now that the branch has been merged, the developer should remove his development
branch.

.. code-block:: console

	$ (master) git branch -d featureA
	$ (master) git push origin :featureA

Stable branches
++++++++++++++++

When we prepare a release, we update CHANGELOG (with our workflow, a
``git log --oneline`` should be quite clear to do that) and tag the branch
``master`` (optional), then we start a stable branch.

.. code-block:: console

	$ (master) git tag 1.0
	$ (master) git checkout -b stable1.0
	$ (stable1.0) git push origin stable1.0

This branch is deployed on different servers.

While development goes on, we possibly have to do some hotfixes (for example: commit
*hf1* in schema below), that must be sent in production quickly.
These hotfixes are done directly on concerned stable branch.

.. image:: /images/010-gw5.png
    :alt: Workflow GIT 5

Regularly, the maintainer merges stable branch in ``master`` to bring back these
commits. This action is particularly important before the next release.

.. code-block:: console

	$ (master) git merge --no-ff stable1.0

We found this method really useful because:

* each stable branch has its own life and doesn't take care of branch ``master`` evolution, so **we can hotfix stable branche freely and without stress**
* we ensure that no hotfix commit has been lost before next release (avoid regressions)

A complete history example
+++++++++++++++++++++++++++

.. image:: /images/010-gw6.png
    :alt: Workflow GIT 6

Conclusion
-----------

Of course, there are several GIT workflows which can be very efficient, but we found
many advantages in working with this method, and no real issue:

* Branch ``master`` is always clean and working well
* Developers don't care about GIT whole workflow
* We can fix stable branch without asking ourselves what happened on ``master`` since last release
* We ensure that each stable release contains new features and possible fixes
* Always working with branches and using``-no-ff``option make history really clear !
* This workflow is scalable (number of developers or branches doesn't really matter)


If you liked this article, stay tuned ! I sometimes `tweet <http://twitter.com/__fle__>`_ and post `GIT articles </tag/git.html>`_ !


[FR] Ce billet en français sur le blog de Makina Corpus : `Un workflow GIT efficace pour les projets à moyen/long terme <http://makina-corpus.com/blog/metier/un-workflow-git-efficace-pour-les-projets-a-moyen-long-terme>`_ !


EDIT : Tag and stable branch should not share the same name. Thanks `regilero <http://twitter.com/regilero>`_ !

.. raw:: html
		
		<style type="text/css">
		    article img {
		    	display: block;
		    	margin: 0 auto;
		    }
		</style>
