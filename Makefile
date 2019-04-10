all: clean source install build package

clean:
	rm -rf tmp
	cd nana-test && make clean

source:
	conan source . --source-folder=tmp/source

install:
	conan install  . --install-folder=tmp/build

build:
	conan build . --source-folder=tmp/source --build-folder=tmp/build

package:
	conan package . -bf=tmp/build -pf=tmp/package

# when you're satisfied that the package is correct, install it for real
package-install:
	conan remove -f nana/1.6.2@ppetraki/nana
	conan create   . ppetraki/nana -s build_type=Release
	conan create   . ppetraki/nana -s build_type=Debug

smoke-test:
	cd nana-test && make debug && build-debug/example
	#cd nana-test && make release && build-release/example
