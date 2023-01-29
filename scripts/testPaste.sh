#!/usr/bin/env bash

source scripts/python.conf 


echo TEST$ $PY_CMD src/tt.py paste
$PY_CMD src/tt.py paste
echo

echo TEST$ $PY_CMD src/tt.py paste data/let3 data/num2
$PY_CMD src/tt.py paste data/let3 data/num2
echo

echo TEST$ $PY_CMD src/tt.py paste data/num2 data/let3
$PY_CMD src/tt.py paste data/num2 data/let3
echo

echo TEST$ $PY_CMD src/tt.py paste data/num2 data/words5 data/let3
$PY_CMD src/tt.py paste data/num2 data/words5 data/let3
echo

echo TEST$ $PY_CMD src/tt.py paste data/num2 data/let3 data/words5
$PY_CMD src/tt.py paste data/num2 data/let3 data/words5
echo

echo TEST$ $PY_CMD src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8
$PY_CMD src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8
echo

echo TEST$ $PY_CMD src/tt.py paste data/ages8 FILE_DNE data/words200
$PY_CMD src/tt.py paste data/ages8 FILE_DNE data/words200
