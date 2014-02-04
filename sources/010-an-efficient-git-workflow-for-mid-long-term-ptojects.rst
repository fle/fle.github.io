An efficient GIT workflow for mid/long term projects
####################################################

:date: 2014-01-31
:tags: git
:category: dev
:author: Florent Lebreton (fle)
:status: draft

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

1. One (and only one) maintainer, who manage GIT repository and releases
2. Never commit directly on ``master``
3. Do not get out of planned workflow

Workflow
---------

Master branch
++++++++++++++

Our branch ``master`` is the common trunk and simply contains all the codebase of
the next release. Since we don't work directly on it, it evolves mainly with merges.

SCHEMA

Development branches
+++++++++++++++++++++

When a developer starts a new feature or a bugfix, he creates a new branch from
``master`` ``HEAD``

.. code-block:: console

	$ (master) git checkout -b featureA
	$ (featureA) git add -m "featureA part 1"
	$ (featureA) git add -m "featureA part 2"

SCHEMA

He follows branch ``master`` evolution and regularly ensures his code still works,
by rebasing his branch ``featureA`` on branch ``master``.

.. code-block:: console

	$ (featureA) git rebase master

When his developments are done, he does a last rebase. Thanks to this:

* he ensures that the maintainer will be able to merge easily (maintainer should not need to read code deeply and search why there are conflicts)
* if tests pass on development branch after rebase, they should pass on ``master`` after merge, so **we ensure that branch ``master`` is always working well**

Possibly, it will be the good time to
`clean the development branch <http://fle.github.io/git-tip-keep-your-branch-clean-with-fixup-and-autosquash.html>`_
to let it neat just when it is finished.

SCHEMA

The maintainer can now merge this branch in ``master`` peacefully, without big
conflict troubles. As the maintainer, I like to use ``no-ff`` option to force a 
*merge commit*, so **history can stay really readable** (we easily see where the
branch has started and where it has been merged).

.. code-block:: console

	$ (master) git merge --no-ff featureA

SCHEMA

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

	$ (master) git tag stable1.0
	$ (master) git checkout -b stable1.0
	$ (stable1.0) git push origin stable1.0

This branch is deployed on different servers.

While development goes on, we possibly have to do some hotfixes, that must be
sent in production quickly. These hotfixes are done directly on concerned stable
branch.

SCHEMA

Regularly, the maintainer merges stable branch in ``master`` to bring back these
commits. This action is particularly important before the next release.

.. code-block:: console

	$ (master) git merge --no-ff stable1.0

We found this method really useful because:

* each stable branch has its own life and doesn't take care of branch ``master`` evolution, so **we can hotfix stable branche freely and without stress**
* we ensure that no hotfix commit has been lost before next release (avoid regressions)

A complete history example
+++++++++++++++++++++++++++

SCHEMA


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