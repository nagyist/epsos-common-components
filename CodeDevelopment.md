# Prerequisites for building the OpenNCP components #

## Git ##

Git on windows: http://msysgit.github.com/

Git on **nix: follow instructions on http://git-scm.com/download/linux**

Git on OSX: http://code.google.com/p/git-osx-installer/

## Maven and Ant ##
The OpenNCP components are built using either ant or maven.

For the projects using maven, please ensure that you are using maven version 3.x or newer.

## Java ##

Most of the components should build with java 1.5 but some of the components require 1.6 or newer. Please consult the `pom.xml` for further specific instructions.

## Editors ##

The development and building of the components is independent of source code editors. Generally, the sources are expected to be in UTF-8 encoding, so the editor should support this.

# Handling of Maven artifacts #

All maven artifacts are planned to be released on joinup.eu, but in our day to day development work, we might need to have snapshot builds exposed as maven artifacts. To this end, we might use github. The following blog-post describes a setup: http://cemerick.com/2010/08/24/hosting-maven-repos-on-github/
It seems that this setup could work here with a google code repository as well.