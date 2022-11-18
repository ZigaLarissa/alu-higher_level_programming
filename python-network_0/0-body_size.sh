#!/bin/bash
# takes in a url and displays its response body size
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
