# vim:ft=meson

project('nana-example',
    'cpp',
    version : '0.1.0',
    # these are overriden by conan so make sure you make changes
    # in both places or you will be "surprised" when you run meson
    # without conan harnessing it.
    default_options : ['warning_level=3',  'cpp_std=c++1z']
    )

cpp_flags = [
   '-Wall',
   '-Wextra',
   '-Wshadow',
   '-Wnon-virtual-dtor',
   '-Wold-style-cast',
   '-Wcast-align',
   '-Wunused',
   '-Woverloaded-virtual',
   '-Wpedantic',
   '-Wconversion',
   '-Wsign-conversion',
   '-Wmisleading-indentation',
   '-Wduplicated-cond',
   '-Wduplicated-branches',
   '-Wlogical-op',
   '-Wnull-dereference',
   '-Wuseless-cast',
   '-Wdouble-promotion',
   '-Wformat=2'
]

link_flags = []

cpp = meson.get_compiler('cpp')
add_project_arguments(cpp.get_supported_arguments(cpp_flags), language : 'cpp')
add_project_link_arguments(cpp.get_supported_link_arguments(link_flags), language : 'cpp')

thread_dep     = dependency('threads', required: true)
fontconfig_dep = dependency('fontconfig', required: true)
xlib_dep       = dependency('x11', required: true)
freetype_dep   = dependency('xft', required: true)
filesystem_dep = cpp.find_library('stdc++fs', required: true)

# provided by conan
nana_dep       = dependency('nana', method : 'pkg-config', required: true)

example_sources = files('''
    src/example.cpp
'''.split())

executable('example',
    example_sources,
    dependencies : [nana_dep, xlib_dep, freetype_dep, fontconfig_dep, filesystem_dep, thread_dep],
    )
