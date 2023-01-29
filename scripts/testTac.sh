#!/usr/bin/env bash

source scripts/python.conf 


echo TEST$ $PY_CMD src/tt.py tac
$PY_CMD src/tt.py tac
echo

echo TEST$ $PY_CMD src/tt.py tac data/let3
$PY_CMD src/tt.py tac data/let3
echo

echo TEST$ $PY_CMD src/tt.py tac data/let3 data/num2
$PY_CMD src/tt.py tac data/let3 data/num2
echo

echo TEST$ $PY_CMD src/tt.py tac data/dup5 data/let3 data/names8 data/num2
$PY_CMD src/tt.py tac data/dup5 data/let3 data/names8 data/num2
echo

echo TEST$ $PY_CMD src/tt.py tac data/let3 FILE_DNE data/num2
$PY_CMD src/tt.py tac data/let3 FILE_DNE data/num2
