TOP=$(shell pwd)
CURRENT_BUILD=${TOP}/current-build

# the release profile is named 'default' for conan, probably should change that.
BUILD_PROFILE=
BUILD_TYPE=

# map build types to conan build profiles
ifeq ($(MAKECMDGOALS), debug)
	BUILD_PROFILE = debug
	BUILD_TYPE = debug
endif

ifeq ($(MAKECMDGOALS), release)
	BUILD_PROFILE = default
	BUILD_TYPE = release
endif

BUILD_DIR := build-$(shell echo $(BUILD_TYPE) | tr A-Z a-z)

# just describe the project and exit if we don't target a build
ifeq ($(BUILD_PROFILE),)
all: info
endif

.PHONY: header
header:
	@echo "BUILD_DIR $(BUILD_DIR)"
	@echo "BUILD_TYPE $(BUILD_TYPE)"

.PHONY: info
info:
	conan info .

clean:
	rm -rf build-* tags current-build compile_commands.json

.PHONY: tags
tags:
	ctags -R src/

.PHONY: build_dispatch
build_dispatch:
	mkdir ${BUILD_DIR} || :
	rm -f current-build && ln -sf ${BUILD_DIR} current-build
	conan install . -pr ${BUILD_PROFILE} --install-folder ${BUILD_DIR}
	conan build   . --build-folder ${BUILD_DIR}
	cp current-build/compile_commands.json ${TOP}
	# fix the path
	sed -i "s/file\": \"..\//file\": \"/g" compile_commands.json

.PHONY: debug
debug: header build_dispatch tags

.PHONY: release
release: header build_dispatch tag

.PHONY: check
check: clean
	make debug
	make release

.PHONY: coverage
coverage:
	cd current-build && ninja coverage
	gcovr ${CURRENT_BUILD}

.PHONY: scan-build
scan-build:
	cd current-build && export PKG_CONFIG_PATH=${CURRENT_BUILD} && ninja scan-build

.PHONY: clang-format
clang-format:
	scripts/clang-format-all kbs/

.PHONY: coverage-html
coverage-html: coverage
	xdg-open file://${CURRENT_BUILD}/meson-logs/coveragereport/index.html

.PHONY: coverage-report
coverage-report: coverage
	gcovr ${CURRENT_BUILD}
