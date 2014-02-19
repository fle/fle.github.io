GIT tip : Keep your branch clean with fixup and autosquash
###########################################################

:date: 2013-12-04
:tags: git
:category: quick tips
:author: Florent Lebreton (fle)

Who is not tired of committing a "Remove pdb" or a "Fix a typo" few minutes or hours after committing a clean feature ? A few time ago, I discovered two useful options in GIT that work together : ``git commit --fixup`` and ``git rebase --autosquash``. With these, you can easily merge little fixes with the original feature and keep your branch clean.

Preferably, you won't use it in a stable or master branch, because rebase rewrites history and can create a big mess, mainly if project counts several developers. It rather can be convenient to clean a development branch before merging it in master.

--fixup & --autosquash
=======================

* ``git commit --fixup <commit>`` automatically marks your commit as a fix of a previous commit
* ``git rebase -i --autosquash`` automatically organize merging of these fixup commits and associated normal commits

Example
========
Take a git repos with a branch `dev`. You intend to commit features A and B:

.. code-block:: console

    $ (dev) git add featureA
    $ (dev) git commit -m "Feature A is done"
    [dev fb2f677] Feature A is done
    $ (dev) git add featureB
    $ (dev) git commit -m "Feature B is done"
    [dev 733e2ff] Feature B is done

Your work is in progress and you find minor mistakes in Feature A : it's time to use ``--fixup`` option !

.. code-block:: console

    $ (dev) git add featureA                # you've removed a pdb : shameful commit
    $ (dev) git commit --fixup fb2f677
    [dev c5069d5] fixup! Feature A is done

Here, you see that GIT automatically retrieved featureA commit message prefixed by fixup!.

All work is done, let's see the log:

.. code-block:: console

    $ (dev) git log --oneline
    c5069d5 fixup! Feature A is done
    733e2ff Feature B is done
    fb2f677 Feature A is done
    ac5db87 Previous commit

Now, you want to clean your branch before merging it : it's time to use ``--autosquash`` option !

.. code-block:: console

    $ (dev) git rebase -i --autosquash ac5db87
    pick fb2f677 Feature A is done
    fixup c5069d5 fixup! Feature A is done
    fixup c9e138f fixup! Feature A is done
    pick 733e2ff Feature B is done

This command has opened your editor with lines above. Just save & quit and ... :

.. code-block:: console

    $ (dev) git log --oneline
    ff4de2a Feature B is done
    5478cee Feature A is done
    ac5db87 Previous commit

Your shameful commit has been merged properly with the original feature. It's just a shorcut for something you could do otherwise but I find it very convenient :).

That's all folks !

EDIT : ``git rebase i <after-this-commit>`` must be launched with as argument `the last commit you want to retain as-is`, not the first one you want to change. 

Thanks `regilero <http://twitter.com/regilero>`_ & `SebCorbin <http://twitter.com/SebCorbin>`_ for reviewing!