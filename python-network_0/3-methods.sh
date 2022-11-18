#!/bin/bash
# takes in url and displays acceptable methods
curl -sI "$1" | grep "Allow" | awk '{print $2 $3 $4}'
