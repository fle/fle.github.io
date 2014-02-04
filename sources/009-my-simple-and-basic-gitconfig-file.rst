My .gitconfig file
###################

:date: 2014-02-04
:tags: git
:category: dev
:author: Florent Lebreton (fle)
:status: draft

As several friends have asked me this, here is my ``~/.gitconfig`` base file. Nothing special, just a few aliases and some syntax highlighting :).

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

	[color "status"]
	        added = yellow
	        changed = green
	        untracked = cyan

	[color "diff"]
	        whitespace = red reverse

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


