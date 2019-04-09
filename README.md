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
#### Install Nana as a conan package
    ./conan-pkg-build.sh

This expects that a "default" and "debug" profile exists, where "default" is the release build.

#### Build and run nana example
    cd nana-test
    make debug
    build-debug/example

Notes
-----

Linking was a trial and error affair. I'm not really sure if the conanfile package should have handled all of this or it's due to the fact that the author hasn't exported public library dependancies in the cmake.

Nana lacks an "install" so I hacked around it in conan to install the include files into the expected location
