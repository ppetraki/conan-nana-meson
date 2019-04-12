from conans import ConanFile, CMake, tools

# Tested on Ubuntu 18.04
# TODO
# - test against 16.04 and 14.04 to determine dependancy gap
# - What's conan's policy for interactive installers? e.g. need boost_filesystem
# - add RH, fedora, and the Suse
# - Windows and Mac? I'm going to need outside contributors for that

class NanaConan(ConanFile):
    name            = "nana"
    version         = "1.6.2"
    license         = "None" # XXX should probably be MIT
    author          = "Peter M. Petrakis  peter.petrakis@protonmail.com"
    url             = "https://github.com/ppetraki/conan-nana-meson.git"
    description     = "A modern C++ GUI library http://nanapro.org"
    topics          = ("gui", "modern-cpp", "cross-platform")
    settings        = "os", "compiler", "build_type", "arch"
    options         = {"shared": [True, False]}
    default_options = "shared=False"
    generators      = "cmake"

    # the preceding was from the boilerplate, the _ stuff is mine.

    #XXX this should *really* be part of the boilerplate, just a like a deb...
    _upstream   = "https://github.com/cnjinhao/nana.git"
    _tag        = "v" + version

    # make this stand out
    _vcs_folder = "nana" + "_" + _tag

    # These calls do not share state. Do not create class or global variables
    # with the intention of writing back state for use later on.
    #
    # probably a good idea to make these calls as close to idempotent as possible too

    def source(self):
        self.run("rm -rf %s" % self._vcs_folder)

        #print(('\x1b[6;30;42m' + "cloning %s at tag %s as detached HEAD to folder:\n %s" + '\x1b[0m')
        #        % (self._upstream, self._tag, self.source_folder + "/" + self._vcs_folder))

        self.run("git clone --branch %s  -- %s %s" %
                (self._tag, self._upstream, self._vcs_folder))

    def build(self):
        cmake = CMake(self)

        # cmake install target is not enabled by default. It installs
        # everything into a package/ under the build dir.
        cmake.definitions["NANA_CMAKE_INSTALL"] = "ON"

        cmake.configure(source_folder=self._vcs_folder)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*",         dst="include", src="package/include")
        self.copy("*nana.lib", dst="lib",     src="package/lib", keep_path=False)
        self.copy("*.dll",     dst="bin",     src="package/bin", keep_path=False)
        self.copy("*.so",      dst="lib",     src="package/lib", keep_path=False)
        self.copy("*.dylib",   dst="lib",     src="package/lib", keep_path=False)
        self.copy("*.a",       dst="lib",     src="package/lib", keep_path=False)

    def package_info(self):
        suffix = "_d" if self.settings.build_type == "Debug" else ""
        libnana = "nana" + suffix

        self.cpp_info.libs = [libnana]

        # build says c++14 but we'll use 11 for a wider audience
        self.cpp_info.cppflags = ["-std=c++11"]
        # derived by build() output NANA_LINKS
        self.cpp_info.libs.append("pthread")
        self.cpp_info.libs.append("X11")
        self.cpp_info.libs.append("Xft")
        self.cpp_info.libs.append("fontconfig")
        # XXX this may be busted outside of 18.04 which will
        # require me to use boost_filesystem
        self.cpp_info.libs.append("stdc++fs")
