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

and of course there's an uninstall

    make package-uninstall

#### Build and run nana example
Once the package is installed, you can try out the sample project against it.

    cd nana-test
    make release
    build-release/example

or from the top

    make smoke-test

A debug target is also provided

    make smoke-test-debug

Notes
-----
Linking was a trial and error affair. It appears that you lose out on the
cmake library dependency forwarding when you package something using conan. Which
makes sense now inretrospect. You're flattening the library into an interface pkg-config can handle.

By observing the build output (e.g. NANA_LINKS) you will see what libraries Nana is linking against and then add them to the package_info() self.cpp_info.libs dictionary.

Nana's Cmake install is OPTIONAL which is not the standard way of doing things. I didn't think to dig into the project when cmake install failed because, why would you
do that? This wasted a lot of energy in packaging that could have been spent elsewhere. It is enabled now and makes the package() step essentially boilerplate code.

I still don't have an answer as to how I'm going to handle system platform dependancies like boost_filesystem over stdc++fs depending on the compiler/platform vintage. Conan doesn't appear to have this fleshed out very well or I'm ignorant to the solution. Time will tell.

The Makefile is used to drive conan package development using this blog post as a guide,

https://bincrafters.github.io/2017/11/10/Updated-Conan-Package-Flow/

Markdown file edited using ReText, which offers editing + live preview.
