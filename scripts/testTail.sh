#!/usr/bin/env bash

source scripts/python.conf 


echo TEST$ $PY_CMD src/tt.py tail
$PY_CMD src/tt.py tail
echo

echo TEST$ $PY_CMD src/tt.py tail data/let3
$PY_CMD src/tt.py tail data/let3
echo

echo TEST$ $PY_CMD src/tt.py tail data/words200
$PY_CMD src/tt.py tail data/words200
echo

echo TEST$ $PY_CMD src/tt.py tail -n 13 data/words200
$PY_CMD src/tt.py tail -n 13 data/words200
echo

echo TEST$ $PY_CMD src/tt.py tail -n 3 data/ages8 data/names8 data/words200
$PY_CMD src/tt.py tail -n 3 data/ages8 data/names8 data/words200
echo

echo TEST$ $PY_CMD src/tt.py tail data/ages8 FILE_DNE data/words200
$PY_CMD src/tt.py tail data/ages8 FILE_DNE data/words200
