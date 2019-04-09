#!/bin/bash
conan source . --source-folder=tmp/source
conan install  . --install-folder=tmp/build
conan build . --source-folder=tmp/source --build-folder=tmp/build
conan package . -bf=tmp/build -pf=tmp/package
