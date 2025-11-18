#!/bin/bash
python3 -m flask_frozen freeze
if [ ! -d "build" ]; then
    echo "ERROR: Frozen-Flask did not generate build/ folder"
    exit 1
fi
echo "Build generated successfully!"
