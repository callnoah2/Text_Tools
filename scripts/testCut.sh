#!/usr/bin/env bash

source scripts/python.conf 


# Need to make files to test from...
echo "Creating data/TMP_people.csv with the built-in paste tool..."
paste -d, data/names8 data/ages8 data/colors8 data/verbs8 > data/TMP_people.csv
echo "Creating data/TMP_kids.csv with the built-in paste tool..."
paste -d, data/num10 data/names10 data/words5 > data/TMP_kids.csv
echo

# clean these files up before the script exits
trap "echo Removing temporary files; rm -f data/TMP_people.csv data/TMP_kids.csv" EXIT


echo TEST$ $PY_CMD src/tt.py cut
$PY_CMD src/tt.py cut
echo

echo TEST$ $PY_CMD src/tt.py cut data/TMP_people.csv
$PY_CMD src/tt.py cut data/TMP_people.csv
echo

echo TEST$ $PY_CMD src/tt.py cut -f 2 data/TMP_people.csv
$PY_CMD src/tt.py cut -f 2 data/TMP_people.csv
echo

echo TEST$ $PY_CMD src/tt.py cut -f 2,4 data/TMP_people.csv
$PY_CMD src/tt.py cut -f 2,4 data/TMP_people.csv
echo

echo TEST$ $PY_CMD src/tt.py cut -f 4,2 data/TMP_people.csv
$PY_CMD src/tt.py cut -f 4,2 data/TMP_people.csv
echo

echo TEST$ $PY_CMD src/tt.py cut -f 2 data/TMP_kids.csv data/TMP_people.csv
$PY_CMD src/tt.py cut -f 2 data/TMP_kids.csv data/TMP_people.csv
echo

echo TEST$ $PY_CMD src/tt.py cut -f 13 data/TMP_people.csv
$PY_CMD src/tt.py cut -f 13 data/TMP_people.csv
echo

echo TEST$ $PY_CMD src/tt.py cut -f 3 data/TMP_kids.csv
$PY_CMD src/tt.py cut -f 3 data/TMP_kids.csv
echo

echo TEST$ $PY_CMD src/tt.py cut data/let3 DOES_NOT_EXIST data/complexity
$PY_CMD src/tt.py cut data/let3 DOES_NOT_EXIST data/complexity
