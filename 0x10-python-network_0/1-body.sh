#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

STATUS="$(curl -s -o /dev/null -w "%{http_code}" "$1")"

if [ "$STATUS" -eq 200 ]
then
  curl -s "$1"
fi