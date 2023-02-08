# Software Development Plan

## Phase 0: Requirements Specification
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [x] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [x] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [x] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [x] List the algorithms that will be used (but don't write them yet).


-My Phase 0, instructions:
**Step One**
[x]Read through all files
**Step Two**
[x]Do it again
**Step three**
[x]Re-write instructions

In this assignment, I will create the following text tools (Preferably in this order):
Cat - WC - Grep - Head - Sort - Tac - Tail - Cut - Paste
User can use all tools by runinng python3 src/tt.py ToolToBeUsed [Options] TheFIle OtherFilesAreOptional
all tools will be ran through Usage.usage(): to help organize code. This file doesn't need to be changed.
when testing, I can check what the output should be by checking the examples to make sure I am doing this right.
	when files are opened, they should be in read only mode. Don't change files
	User input is from a driver, not an input function. 
I need to create error messages by mimicing the Unix text tools. Usage.usage() will be used to give consitant error messages
	Some erros will be detected in the driver,
	Others will be detected by the tool itself.
		errors will include: 
		too few arguments
		invalid tool selection
		file does not exist
		non file object cannot be opened
		User Does not have permission to view this file
		too few or incorect arguments given

**Step four**
[x]Explain what each function should do
	* what input it needs 
	* what will cause error messages and what the messages will say
	* any challenges with the function
	* what I already know how to do

Cat - can take >= 1 files, The cat function will open the files it is given and print them into one output.
error - file does not exist
error - User does not have permission to view this file
error - Too few arguments

WC - can take >= 1 files, output is one line per file giving the user:
	the number of lines,
	the number of words,
	the number of characters.
	the file the data came from. 
words will be seperated by space, so even if the word is hello-this-is-one-word, it is counted as one word.
output must be formatted in a way that each column is seperate
error - file does not exist
error - too few arguments given
these errors do not need to be pre - screened, open will raise an exception

Grep - this function is case sensitive, this function takes an argument, -v, where it finds all lines not containing the argument being searched for.
errors will be handled with the open() function

Head - This function will print off the first 10 lines of a file, therefore, if a file has <= 10 lines, it will act as the cat function. different limits can be set with the -n argument
I will need to convert this argument into a number
when multiple files are opened, it will seperate files and print them as one output
Open() function will raise all errors

Sort - sort will print a file were each line is sorted in lexical order.
when multiple files are given, the lines will be mixed.
errors will be caught with the open() function

Tac - can take >= 1 files, opens the files and prints them into one output, but in reverse.
same errors as cat

Tail - This function will print the final 10 lines of a file, uses the -n argument to set a different limit. 
multiple files will be seperated and printed in the same output.
open() will raise all erros

Cut - this function will extract columns from a single file, lines are split into fields on each comma, by defalt the first field is printed but the rest are ignored
-f can be given as an argument to specify which field to extract by number, by default, cut's field numbers start with a 1 and not a 0
-f can take multiple arguments to cut multiple fields, seperate with a comma, and print them
cut can take multiple inputs of files.
Field numbers greater than teh number of fields present in a file are treated as they are empty, do this to prevent an Index error
open() will raise exeptions

Paste - paste will join two or more files together with a comma seperating them. paste works by opening a file and using a for loop to iterate through the list of file objects
reading one line from each file and priting it with a comma and not a new line. After the last file is readm a newline is printe, The for loop will be repeated until all files are 
exhausted.
when just one file is given to paste, it acts as cat.
errors are same as cut.

**Step Five**
[x]Data used by functions and where it comes from
	* Explain what form the output will take?

Data all comes from the data files that will be used for testing, really, any text based files can be used as data.
the output will depend on the function called, but it will always be printed out or > directed into a different file.

**Step Six**
[x] List all algorithms that will be used and where
Algorithms will be used to iterate throughe the files given,
they will be used to print the lines line by line
they will be used to reverse the lines in cat
they will be used to search for words

## Phase 1: Design
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [x] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [x] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing


**Algorithm used to iterate through files given**
for loop range len filesgiven
	code to be done for each file one at a time
	iterate loop
**Algorithm used to iterate 


**Functions for each tool:**
Cat -
loop to iterate through files -listed above-
open([file to be opened])
print(new file?)

WC -
open([file])
len of file? 
number of lines
number of characters

grep -
open([file])
for i in len(file)
	if i == "grep word"
		print(grep word)
	i += 1

head -
open([file])
for i in range(10 or change)
	print line
	i += 1

sort -
for loop to iterate through all files,
append a list for each file while using sort function 
print(list)

tac -
cat()
last = len(file by lines)
for last to 1
print line
last -= 1

tail -
open([file])
lines = len of file - 10 or number asked for
for lines in range of len of file
print line
lines += 1

cut -
open([file])
Not sure

paste - 
Not sure

## Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 3: Testing and Debugging
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 4: Deployment
*(5% of your effort)*

Deliver:

*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
