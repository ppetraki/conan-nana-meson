conan-nana-meson
======

Introduction
------------

This is a POC showing how to take an standalone library, in this case nana, and turn it into a conan package.

That package is then leveraged in "nana-test" using meson.

Tested on Ubuntu 18.04

Prerequisites
----
- conan 1.10
- meson 0.49

Both are provided in debs/

Usage
----
#### Packaging workflow
Taken from best practices blogged here:
https://bincrafters.github.io/2017/11/10/Updated-Conan-Package-Flow/

There is a makefile target for each stage of the packaging workflow

The default makefile target invokes all of the prototyping stages + clean.

#### Install Nana as a conan package
Unconditionally removes the existing installed version (1.6.2) and then builds and installs both Release and Debug builds.

    make package-install

#### Build and run nana example
Once the package is installed, you can try out the sample project against it.

    cd nana-test
    make debug
    build-debug/example

or from the top

    make smoke-test

Notes
-----

Linking was a trial and error affair. I'm not really sure if the conanfile package should have handled all of this or it's due to the fact that the author hasn't exported public library dependancies in the cmake.

Nana lacks an "install" so I hacked around it in conan to install the include files into the expected location

The Makefile was used to drive conan package development using this blog post as a guide


Markdown file edited using ReText, which offers editing + live preview.