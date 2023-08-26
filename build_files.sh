#!/bin/bash

echo "BUILD START"

# Create a virtual environment
python3.9 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run collectstatic without prompting for confirmation
python3.9 manage.py collectstatic --noinput

# Deactivate the virtual environment
deactivate

echo "BUILD END"
