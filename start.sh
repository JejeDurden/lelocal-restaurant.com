#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn lelocal.wsgi:application --log-file
