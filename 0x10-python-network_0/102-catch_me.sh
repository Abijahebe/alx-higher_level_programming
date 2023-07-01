#!/bin/bash

curl -s -o response.txt 0.0.0.0:5000/catch_me && grep -o "You got me!" response.txt>&2
