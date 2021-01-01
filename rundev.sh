#!/usr/bin/env bash
set -a
. ./.env
set +a

# python main.py
celery -A main worker -B -Q celery -l DEBUG