all: source install build package

source:
	conan source . --source-folder=tmp/source

install:
	conan install  . --install-folder=tmp/build

build:
	conan build . --source-folder=tmp/source --build-folder=tmp/build

package:
	conan package . -bf=tmp/build -pf=tmp/package

clean:
	rm -rf tmp
