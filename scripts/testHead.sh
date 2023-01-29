#!/usr/bin/env bash

source scripts/python.conf 


echo TEST$ $PY_CMD src/tt.py head
$PY_CMD src/tt.py head
echo

echo TEST$ $PY_CMD src/tt.py head data/let3
$PY_CMD src/tt.py head data/let3
echo

echo TEST$ $PY_CMD src/tt.py head data/words200
$PY_CMD src/tt.py head data/words200
echo

echo TEST$ $PY_CMD src/tt.py head -n 13 data/words200
$PY_CMD src/tt.py head -n 13 data/words200
echo

echo TEST$ $PY_CMD src/tt.py head -n 3 data/ages8 data/names8 data/words200
$PY_CMD src/tt.py head -n 3 data/ages8 data/names8 data/words200
echo

echo TEST$ $PY_CMD src/tt.py head data/ages8 FILE_DNE data/words200
$PY_CMD src/tt.py head data/ages8 FILE_DNE data/words200
