#!/usr/bin/env bash

source scripts/python.conf


echo TEST$ $PY_CMD src/tt.py cat
$PY_CMD src/tt.py cat
echo

echo TEST$ $PY_CMD src/tt.py cat data/let3
$PY_CMD src/tt.py cat data/let3
echo

echo TEST$ $PY_CMD src/tt.py cat data/let3 data/num2
$PY_CMD src/tt.py cat data/let3 data/num2
echo

echo TEST$ $PY_CMD src/tt.py cat data/dup5 data/let3 data/names8 data/num2
$PY_CMD src/tt.py cat data/dup5 data/let3 data/names8 data/num2
echo

echo TEST$ $PY_CMD src/tt.py cat data/let3 FILE_DNE data/num2
$PY_CMD src/tt.py cat data/let3 FILE_DNE data/num2
