#!/bin/sh

set -e

uvicorn main:app --host 0.0.0.0 --port 8000