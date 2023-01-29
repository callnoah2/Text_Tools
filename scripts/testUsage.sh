#!/usr/bin/env bash

source scripts/python.conf 


echo TEST$ $PY_CMD src/tt.py
$PY_CMD src/tt.py
echo

echo TEST$ $PY_CMD src/tt.py cat
$PY_CMD src/tt.py cat
echo

echo TEST$ $PY_CMD src/tt.py tac
$PY_CMD src/tt.py tac
echo

echo TEST$ $PY_CMD src/tt.py head
$PY_CMD src/tt.py head
echo

echo TEST$ $PY_CMD src/tt.py tail
$PY_CMD src/tt.py tail
echo

echo TEST$ $PY_CMD src/tt.py grep
$PY_CMD src/tt.py grep
echo

echo TEST$ $PY_CMD src/tt.py wc
$PY_CMD src/tt.py wc
echo

echo TEST$ $PY_CMD src/tt.py sort
$PY_CMD src/tt.py sort
echo

echo TEST$ $PY_CMD src/tt.py paste
$PY_CMD src/tt.py paste
echo

echo TEST$ $PY_CMD src/tt.py cut
$PY_CMD src/tt.py cut
