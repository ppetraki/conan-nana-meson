from conans import ConanFile, Meson

class ExampleConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    # ("", "")
    requires = ("nana/1.6.2@ppetraki/nana")

    generators = "pkg_config", "ycm"

    default_options = {"gtest:shared": True}

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin

    def build(self):
        meson = Meson(self)

        # conan is shadowing these meson parameters...
        args=[]
#        args = ['-Db_coverage=true']
#        args = ['-Db_coverage=true', '-Db_sanitize=address']
        options={ 'warning_level': 3, 'cpp_std': 'c++1z'}
        meson.configure(args=args, defs=options)

        meson.build()
        # XXX probably move all makefile magic to here
    #    meson.test()
    #    meson.test(targets=['coverage'])
