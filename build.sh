#!/bin/bash
echo "Building ShareVolume static site..."

# Freeze Flask app into static files
python3 -m flask_frozen freeze

if [ ! -d "build" ]; then
    echo "ERROR: build/ folder not found"
    exit 1
fi

echo "Build generated successfully!"
