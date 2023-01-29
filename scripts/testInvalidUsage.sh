#!/usr/bin/env bash

source scripts/python.conf 


echo TEST$ $PY_CMD src/tt.py head -n data/forgot_number
$PY_CMD src/tt.py head -n data/forgot_number
echo

echo TEST$ $PY_CMD src/tt.py tail -n data/forgot_number
$PY_CMD src/tt.py tail -n data/forgot_number
echo

echo TEST$ $PY_CMD src/tt.py grep ONLY_PATTERN
$PY_CMD src/tt.py grep ONLY_PATTERN
echo

echo TEST$ $PY_CMD src/tt.py grep -v ONLY_PATTERN
$PY_CMD src/tt.py grep -v ONLY_PATTERN
echo

echo TEST$ $PY_CMD src/tt.py cut -f data/forgot_field
$PY_CMD src/tt.py cut -f data/forgot_field
