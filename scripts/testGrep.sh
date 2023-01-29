#!/usr/bin/env bash

source scripts/python.conf 


echo TEST$ $PY_CMD src/tt.py grep
$PY_CMD src/tt.py grep
echo

echo TEST$ $PY_CMD src/tt.py grep Blue data/colors8
$PY_CMD src/tt.py grep Blue data/colors8
echo

echo TEST$ $PY_CMD src/tt.py grep blue data/colors8
$PY_CMD src/tt.py grep blue data/colors8
echo

echo TEST$ $PY_CMD src/tt.py grep a data/ages8 data/colors8 data/let3
$PY_CMD src/tt.py grep a data/ages8 data/colors8 data/let3
echo

echo TEST$ $PY_CMD src/tt.py grep -v a data/ages8 data/colors8 data/let3
$PY_CMD src/tt.py grep -v a data/ages8 data/colors8 data/let3
echo

echo TEST$ $PY_CMD src/tt.py grep a data/ages8 FILE_DNE data/words200
$PY_CMD src/tt.py grep a data/ages8 FILE_DNE data/words200
