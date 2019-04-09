#!/bin/bash
rm -rf ~/.conan/data/Nana/1.6.2/
conan create . ppetraki/nana -pr default
conan create . ppetraki/nana -pr debug
