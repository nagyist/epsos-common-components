# Introduction #

First off: thank you for considering contributing code to the epSOS OpenNCP project!

On this page, you will hopefully find all the information necessary to create, submit and successfully having your patch accepted.

# Creating a patch #

First of all, you should create an issue in the issuetracker which describes the reasons for the patch. Your commit history should contain the issue id.

The official git wiki http://git-scm.com/ has great instructions for creating patches:

a happy path of creating a patch would look like:
```
$ git clone https://code.google.com/p/epsos-core-components
$ cd epsos-core-components
$ (edit/add files)
$ git add (files)
$ git commit -m '[(issue id)] Explain what I changed'
$ {iterate the three above actions}
$ git format-patch origin/master
```

You can also dive into the [man page](http://man.he.net/man1/git-format-patch)

If you're not already listed in the `CREDITS.txt` file, please add yourself, with the same information you use for your git author information.

# Coding guidelines for patches #

Please **do**:

  * try to adhere to the coding style of files you edit;
  * comment code whose function or rationale is not obvious;
  * update documentation (e.g., package.html files, this wiki, etc.)

Please do **not**:

  * reformat code unrelated to the bug being fixed: formatting changes should be separate patches/commits.
  * comment out code that is now obsolete: just remove it.
  * insert comments around each change, marking the change: folks can use the commit history to figure out what's changed and by whom.
  * make things public which are not required by end users.
  * Add `@author` tags to your code. (you will be credited in the `CHANGES.txt` file).

# Guidelines for git commit messages #

Generally, there exists two kinds of commits: those involving business logic changes, and those that don't.

For commits involving business logic changes, it is preferable that we have a reference to a jira issue from http://openncp.atlassian.net. This not only helps other developers understand the reason for the commits, it also makes repository housekeeping immensely easier.

For other types of commits, please write at least a summary describing the changes made. Please **do not** just write generic comments, such as "fixed files" or "made changes". use `git add -p` to separate the commit in logical parts.

This [blog post](http://who-t.blogspot.dk/2009/12/on-commit-messages.html) has some good general advice for creating git commit messages

# Unit testing your patch #

For an easy and safe itegration of your patch, please provide unittests of all publicly accessible, non-trivial methods and all integration points. We don't aim for 100% code-coverage, but enough to make us comfortable that we're not breaking expected and/or specified behaviour.

# Contributing the patch #

Attach the patch to the issue pertaining to the patch. If and hopefully when your patch is accepted, your name (taken from the `CREDITS.txt` file) will be added to the `CHANGES.txt` file along with the issue id, and your patch will be merged with the master branch or the specific branch you have made your `git format-patch` against.