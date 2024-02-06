# CS 1440 Assignment 2: Text Tools - Test Scripts

This directory contains simple *shell scripts* to help you conveniently test your Text Tools.

Compare the output produced by these programs with what is shown in the [Examples of Expected Output](../instructions/examples).

**IMPORTANT!!**

*   These scripts must be run from the project's root directory!
*   The scripts will not work if you rename `src/tt.py`!


## Table of Contents

*   [Configuring `python.conf`](#configuring-python.conf)
*   [Running The Scripts](#running-the-scripts)
*   [Saving Output To Text Files](#saving-output-to-text-files)
*   [Understanding Shell Scripts](#understanding-shell-scripts)


## Configuring `python.conf`

Because everyone at DuckieCorp uses different computers, the command for Python 3 varies.  [`python.conf`](python.conf) tries to auto-detect your Python interpreter.  It usually works!  But if it fails, edit this file to use the same Python command that you use on the command line.


## Running The Scripts

*   [`testUsage.sh`](testUsage.sh)
    *   Give various inputs to `tt.py` that will result in different usage messages
*   [`testCat.sh`](testCat.sh)
*   [`testTac.sh`](testTac.sh)
*   [`testHead.sh`](testHead.sh)
*   [`testTail.sh`](testTail.sh)
*   [`testGrep.sh`](testGrep.sh)
*   [`testWC.sh`](testWC.sh)
*   [`testSort.sh`](testSort.sh)
*   [`testPaste.sh`](testPaste.sh)
*   [`testCut.sh`](testCut.sh)
*   [`testInvalidUsage.sh`](testInvalidUsage.sh)
    *   Tests a few tools with invalid command lines

**Important** These scripts *must* be run from the project's root directory.  For example:

```
$ scripts/testUsage.sh
TEST$ python src/tt.py
Python Text Tools Usage
=======================

tt.py cat|tac FILENAME...
    Concatenate and print files in order or in reverse

... remaining output omitted ...
```

The other scripts will only do the right thing once you complete the corresponding tool.


## Saving Output To Text Files

Use the *special* shell redirection operator `&>` to save a test script's output into a file.  In contrast to the redirection operator `>`, `&>` combines ordinary output from `STDOUT` with error messages from `STDERR` into one file.

```
~/cs1440-assn2 $ ./scripts/testUsage.sh &> UsageTest.log
~/cs1440-assn2 $ cat UsageTest.log
$ python src/tt.py
Python Text Tools Usage
=======================

tt.py cat|tac FILENAME...
    Concatenate and print files in order or in reverse
...
```

## Understanding Shell Scripts

Understanding how these scripts work is not part of this assignment.  But in case you are curious, I will explain a few features of the scripts:

*   `#!/usr/bin/env bash`
    *   This is called the *shebang line*
    *   It tells the OS how to execute this text file
        *   In this case, the OS runs this file in the Bash shell
    *   `#` introduces a comment, just like in Python
        *   Once `bash` takes over the execution of this file, the shebang line is treated as an ordinary comment 
*   `source FILE`
    *   Read `FILE` and execute its contents *without launching a new shell process*
    *   This sets the variable `PY_CMD=python`
    *   Without `source`, the variable `PY_CMD` would **not** be set
*   `PY_CMD=''`
    *   Declare a new variable and assign to it the empty string
    *   Like Python, assignments in the Shell use `=`
    *   Unlike Python, white space *cannot* surround the `=` operator!
    *   It is common for the names of Shell variables to be *UPPER_CASE*
*   `$PY_CMD`
    *   Access the value stored in the `PY_CMD` variable
    *   `$` *expands* a variable into its value
    *   Otherwise, `PY_CMD` would be treated as the string `"PY_CMD"` instead of being replaced with the name of your computer's Python interpreter
    *   Do not use `$` when *assigning* a value to a variable!
*   `echo "TEST$ ..."`
    *   Print the command that is about to be run
*   `$PY_CMD src/tt.py ...`
    *   Execute `src/tt.py` using your computer's preferred Python interpreter
*   `echo`
    *   Print a blank line
