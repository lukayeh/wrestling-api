#!/bin/sh

export APP_MODULE="app.main:app"
export HOST="0.0.0.0"
export PORT="5000"

exec uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"
