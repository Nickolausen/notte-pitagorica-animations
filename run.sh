#! /bin/bash

source .venv/bin/activate
LEVEL="m"

# get flags
while getopts "lmh:" arg; do
  case $arg in
    l|m|h) LEVEL=$arg; shift;;
  esac
done

eval "manim -pq$LEVEL $1"