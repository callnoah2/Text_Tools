#!/usr/bin/env bash

source scripts/python.conf 


echo "NOTE: The *byte count* on Windows might slightly differ"

echo TEST$ $PY_CMD src/tt.py wc
$PY_CMD src/tt.py wc
echo

echo TEST$ $PY_CMD src/tt.py wc data/num2
$PY_CMD src/tt.py wc data/num2
echo

echo TEST$ $PY_CMD src/tt.py wc data/wordcount
$PY_CMD src/tt.py wc data/wordcount
echo

echo TEST$ $PY_CMD src/tt.py wc data/let3 data/random20 data/words200 data/dup5 data/complexity
$PY_CMD src/tt.py wc data/let3 data/random20 data/words200 data/dup5 data/complexity
echo

echo TEST$ $PY_CMD src/tt.py wc data/ages8 FILE_DNE data/words200
$PY_CMD src/tt.py wc data/ages8 FILE_DNE data/words200
