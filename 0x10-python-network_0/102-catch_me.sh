#!/bin/bash

# Make a request to the server and save the response in a file
response_file=$(mktemp)
curl -s -o "$response_file" "0.0.0.0:5000/catch_me"

# Extract the message from the ressponse file
message=$(grep -o "You got me!" "$response_file")

# Display the message without using echo or cat
exec 1>&2
printf '%s\n' "$message"
