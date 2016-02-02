#!/bin/bash

VERSION_peewee=${VERSION_peewee:-2.7.3}
DEPS_peewee=(python)
URL_peewee=https://github.com/coleifer/peewee/archive/$VERSION_peewee.zip
MD5_peewee=
BUILD_peewee=$BUILD_PATH/peewee/$(get_directory $URL_peewee)
RECIPE_peewee=$RECIPES_PATH/peewee

function prebuild_peewee() {
	true
}

function shouldbuild_peewee() {
	if [ -d "$SITEPACKAGES_PATH/peewee" ]; then
		DO_BUILD=0
	fi
}

function build_peewee() {
	cd $BUILD_peewee

	push_arm
	try $HOSTPYTHON setup.py install
	pop_arm
}

function postbuild_peewee() {
	true
}
