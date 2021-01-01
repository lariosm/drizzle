#!/usr/bin/env bash
set -a
. ./.env
set +a

# python main.py
celery -A tasks worker -B -Q celery -l DEBUG