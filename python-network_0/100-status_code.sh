#!/bin/bash
#display the status code of a url only
curl -sI -o /dev/null --write-out '%{http_code}' "$1"
