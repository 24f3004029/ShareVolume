#!/bin/bash
rm -rf build
mkdir build
FLASK_APP=app.py python3 -m flask_frozen freeze
cp -r static build/static
echo "Static site generated in build/"
