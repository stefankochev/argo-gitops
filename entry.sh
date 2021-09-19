#!/bin/bash
# exit by default on all errors
set -e

gunicorn app:app --bind 0.0.0.0:5000 --workers=2