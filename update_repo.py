#!/bin/bash

PY_BIN='/bin/env python'
SRC_DIR=src
REPO_DIR=repo
REPO_NAME=repository.tuffnerdstuff

# Create addons.xml
cd $SRC_DIR
$PY_BIN addons_xml_generator.py
mv addons.xml ../$REPO_DIR
mv addons.xml.md5 ../$REPO_DIR

# Clear repo dir
rm -r ../$REPO_DIR/*

# Create ZIP files
for d in $(find . -mindepth 1 -maxdepth 1 -type d);
do mkdir ../$REPO_DIR/$d; zip -r ../$REPO_DIR/$d/$d.zip $d;
done
cd ..


