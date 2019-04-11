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

# provided by conan
nana_dep       = dependency('nana', method : 'pkg-config', required: true)

example_sources = files('''
    src/example.cpp
'''.split())

executable('example',
    example_sources,
    dependencies : [nana_dep],
    )
