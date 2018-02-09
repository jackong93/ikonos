#!/bin/bash
python manage.py db upgrade
env PYTHONPATH=$PYTHONPATH:$PWD/ikonos
gunicorn run:app --daemon
python worker.py