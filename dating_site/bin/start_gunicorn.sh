#!/bin/bash
exec gunicorn --bind 0.0.0.0:8000 --reload config.wsgi