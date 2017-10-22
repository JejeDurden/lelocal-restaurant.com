#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn lelocal.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3
