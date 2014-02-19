GIT tip : A simple .gitconfig file
###################################

:date: 2014-02-04
:tags: git
:category: development
:author: Florent Lebreton (fle)
:summary: As several friends have asked me this, I have posted my simple but quite useful .gitconfig file. Nothing special here, just a few aliases and some syntax highlighting :).

As several friends have asked me this, here is my ``~/.gitconfig`` base file.

Nothing special, just a few aliases and some syntax highlighting :).

.. code-block:: console

	[user]
	        name = Florent Lebreton
	        email = florentlebreton@free.fr
	[color]
	        ui = auto

	[color "branch"]
	        current = yellow reverse
	        local = yellow
	        remote = green

	[color "diff"]
	        meta = yellow bold
	        frag = magenta bold
	        old = red bold
	        new = green bold
	        whitespace = red reverse

	[color "status"]
	        added = yellow
	        changed = green
	        untracked = cyan

	[core]
	        whitespace=fix,-indent-with-non-tab,trailing-space,cr-at-eol

	[alias]
	        st = status
	        ci = commit
	        br = branch
	        co = checkout
	        df = diff
	        dc = diff --cached
	        lg = log -p
	        pr = pull --rebase
	        gr = log --all --graph --decorate --oneline

&nbsp;

Simple and basic but I hope you'll have found something useful in it. If yes, you may want to know that I sometimes `tweet <http://twitter.com/__fle__>`_ and post `stuff about GIT </tag/git.html>`_ !

Thanks `opidentica <https://twitter.com/opidentica>`_ for having noticed the error!

