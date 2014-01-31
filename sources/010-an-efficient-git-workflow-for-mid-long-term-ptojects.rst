An efficient GIT workflow for mid/long term projects
####################################################

:date: 2014-01-31
:tags: git
:category: python
:author: Florent Lebreton (fle)
:status: Draft

Our CAMM project `JOB <http://makina-corpus.com/realisations/application-de-gmao>`_
at `Makina Corpus <http://makina-corpus.com>`_ has been going on for nearly two
years and is in production for over 18 months. And I think it's my first project
without any headache about our codebase and VCS management.

So, I'll present our GIT workflow which has proven to be very effective for now.

Context
--------

* Several developers
* Several staging/pre-production servers, several non-synchronous production servers
* Monthly releases (more or less) with delivery on staging servers, then on production servers
* On servers, basecode is directly pulled from the GIT repository with fabric

Rules
------

To handle this, we have set some rules:

* We have designated only one maintainer, who manage GIT repository and releases
* Nobody commits directly on  branch *master*
* Do not get out of planned workflow

Workflow
---------

Master branch
++++++++++++++

Our branch *master* is the trunk, it simply contains codebase of the next release.

SCHEMA

Development branches
+++++++++++++++++++++

When a developer starts a new feature or a bugfix, he creates a new branch from
master HEAD

.. code-block:: console

	$ (master) git checkout -b featureA
	$ (featureA) git add -m "featureA part 1"
	$ (featureA) git add -m "featureA part 2"

SCHEMA

He follows branch *master* evolution and regularly ensures his code still works,
by rebasing his featureA branch on branch *master*.

.. code-block:: console

	$ (featureA) git rebase master

When his developments are done, he does a last rebase. It's important because:

* he ensures that the maintainer will be able to merge easily (he should not
need to read code deeply and search why there are conflicts)
* if tests pass on development branch after rebase, they should pass on master
after merge, so we ensure that branch *master* is always working well

Possibly, it will be the good time to
`clean the development branch <http://fle.github.io/git-tip-keep-your-branch-clean-with-fixup-and-autosquash.html>`_
to let it finished and neat.

SCHEMA

The maintainer can now merge this branch in master peacefully. As the maintainer,
I like to use ``no-ff`` option to force a commit merge, so history can be really
readable (we see easily where the branch has started and where it has been merged).

.. code-block:: console

	$ (master) git merge --no-ff featureA

SCHEMA

Now that the branch has been merged, developer should remove his development branch.

.. code-block:: console

	$ (master) git branch -d featureA
	$ (master) git push origin :featureA

Stable branches
++++++++++++++++

When we prepare a release, we do a tag (optional), then we start a stable branch.

.. code-block:: console

	$ (master) git tag stable1.0
	$ (master) git checkout -b stable1.0
	$ (stable1.0) git push origin stable1.0

This branch is deployed on different servers.

While development goes on, we possibly have to do some hotfixes, that must be
sent in production quickly. These hotfixes are done directly on concerned stable
branch.

SCHEMA

Regularly, ther maintainer merges stable branch in master to bring back these
commits. This action is particularly important before the next release.

.. code-block:: console

	$ (master) git merge --no-ff stable1.0

We found this method useful because:

* each stable branch has its own life without taking care of branch *master* evolution
* we ensure that no hotfix commit has been lost (avoid regressions)

A complete history example
+++++++++++++++++++++++++++

SCHEMA


Conclusion
-----------

Of course, there several GIT workflows which can be very efficient, but we found
many advantages in working with this method, and no real issue:

* Branch *master* is always clean and working well
* Developers don't care about GIT whole workflow
* We ensure a stable release contains new features and possible fixes
* Always working with branches and using``-no-ff``option make history really clear !


