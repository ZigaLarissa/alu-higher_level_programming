#!/bin/bash
# takes in url and displays acceptable methods
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2-
