# Avoid the commit message "merge branch 'master'" #

This happens because a `git pull` automatically merge changes from the origin into the master branch locally. The commit messages are effectively noise, as the information is still preserved in the git log.

To avoid the messages, use `git fetch` followed by `git rebase origin/master`. `git fetch` will fetch the changes from the origin, but not apply them to the local repository. This way, it is also possible to review which changes will be made, before applying them. `git rebase origin/master` will reapply every commit of a branch on top of the destination branch, leaving you with only the commit messages of the actual commits.