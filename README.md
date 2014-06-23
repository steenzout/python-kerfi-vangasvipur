# python-kerfi-vangasvipur

[![Build Status](https://travis-ci.org/steenzout/python-kerfi-vangasvipur.svg?branch=master)](https://travis-ci.org/steenzout/python-kerfi-vangasvipur)
[![Code Health](https://landscape.io/github/steenzout/python-kerfi-vangasvipur/master/landscape.png)](https://landscape.io/github/steenzout/python-kerfi-vangasvipur/master)
[![Coverage Status](https://coveralls.io/repos/steenzout/python-kerfi-vangasvipur/badge.png)](https://coveralls.io/r/steenzout/python-kerfi-vangasvipur)
[![Requirements Status](https://requires.io/github/steenzout/python-kerfi-vangasvipur/requirements.png?branch=master)](https://requires.io/github/steenzout/python-kerfi-vangasvipur/requirements/?branch=master)

Python tools to manipulate output from the OSX system_profiler.

It uses:

- [git](http://git-scm.com) for version control
- [pip](http://www.pip-installer.org/en/latest/) to manage Python packages
- [tox](http://tox.readthedocs.org/en/latest/) for automation and setup development environments
- [Sphinx](http://sphinx-doc.org) for documentation


## usage

### kv-print

Using stdout:
```
$ cat tests/input.txt | kv-print -t raw "Applications.Console.Version"
Applications.Console.Version	10.9
```

Using a file and a regular expression:
```
$ kv-print -f tests/input.txt "Applications\.Console.*"
Applications.Console.Location	/Applications/Utilities/Console.app
Applications.Console.Kind	Intel
Applications.Console.64-Bit_(Intel)	Yes
Applications.Console.Version	10.9
Applications.Console.Obtained_from	Apple
Applications.Console.Signed_by	Software Signing, Apple Code Signing Certification Authority, Apple Root CA
```

When using a file as input you don't need to set the format option.


## kerfi

Kerfi means in system in icelandic.

This is the directory which will hold your files.


## docs

Directory where you'll store the [Sphinx](http://sphinx-doc.org) configuration files and
where the documentation will be generated.


## .gitignore

File where you specify which files [Git](http://en.wikipedia.org/wiki/Git_(software)) should ignore.

A generic file has been provided.

You can use [gitignore.io](http://www.gitignore.io) to
produce other files that will better suit your development environment.

For more information, you can check "[git-scm.com : gitignore](http://git-scm.com/docs/gitignore)".


## LICENSE

The Apache 2 license.


## pytest.ini

The [pytest](https://pytest.org/latest/index.html) configuration file.

You can read
"[pytest : Changing standard (Python) test discovery](https://pytest.org/latest/example/pythoncollection.html)"
for more information on how to use this file to customize [pytest](https://pytest.org/latest/index.html)'s behavior.


## README.md

This file.

Check "[here](http://daringfireball.net/projects/markdown/syntax)" for help
with [Markdown](http://daringfireball.net/projects/markdown/) syntax.


## requirements.txt

On this file you specify the list of packages the project depends.

Read "[pip : Requirement Files](http://www.pip-installer.org/en/latest/user_guide.html#requirements-files)"
to understand how you can properly use this file to define your project's dependencies.


## setup.py

The setup script whre you'll describe the project / product, authors, maintainers and
information on how to distribute it.

Read "[Python : 2. Writing the Setup Script](http://docs.python.org/2/distutils/setupscript.html)",
for more information.


## tests

The directory where you should add your unit tests.


## test-requirements.txt

On this file you specify the list of packages the project needs to run its tests.

An example of the possible contents of this file has been provided.

Read "[pip : Requirement Files](http://www.pip-installer.org/en/latest/user_guide.html#requirements-files)"
to understand how you can properly use this file to define your project's test dependencies.


## tox.ini

The [tox](http://tox.readthedocs.org/en/latest/) configuration file.

It contains basic information about your project and test environments.

I recommend [installling tox](http://tox.readthedocs.org/en/latest/install.html) and
use it to run your tests and generate the documentation.

```
# run the tests
$ tox

# generate the documentation
$ tox -e docs
```
