#!/bin/bash
# exit by default on all errors
set -e

gunicorn app:app --bind localhost:5000 --workers=2