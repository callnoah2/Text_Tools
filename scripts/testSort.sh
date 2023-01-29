#!/usr/bin/env bash

source scripts/python.conf 


echo "NOTE: The *byte count* on Windows might slightly differ"
echo

echo TEST$ $PY_CMD src/tt.py sort
$PY_CMD src/tt.py sort
echo

echo TEST$ $PY_CMD src/tt.py sort data/colors8
$PY_CMD src/tt.py sort data/colors8
echo

echo TEST$ $PY_CMD src/tt.py sort data/random20
$PY_CMD src/tt.py sort data/random20
echo

echo TEST$ $PY_CMD src/tt.py sort data/complexity
$PY_CMD src/tt.py sort data/complexity
echo

echo TEST$ $PY_CMD src/tt.py sort data/colors8 data/names10
$PY_CMD src/tt.py sort data/colors8 data/names10
echo

echo TEST$ $PY_CMD src/tt.py sort data/colors8 FILE_DNE data/names10
$PY_CMD src/tt.py sort data/colors8 FILE_DNE data/names10
