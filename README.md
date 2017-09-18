Please find below the exercises comprising this assignment.
Add a solution file for each exercise (where applicable).

# 1. Iterate over a list

First we are going to make a list and fill it with a simple sequence. Then we are going to use this list to print something.
- Make a list containing the numbers 0, 1, ... 9.
- Print the last 10 lines of the song ''99 bottles of beer'' using this list.

# 2. Analyse a repeat structure

We are going to make a repeating DNA sequence and extract some subsequences from it.
- Make a short tandem repeat that consists of three "ACGT" units and five "TTATT" units.
- Print all suffixes of the repeat structure.
  - **Note**: A suffix is an ending. For example, the word "spam" has five suffixes: "spam", "pam", "am", "m" and "".
- Print all substrings of length 3.
- Print all unique substrings of length 3.

**Hint**: All elements in a set are unique.

# 3. Boolean comparison

Try to guess the outcome of the following statements:

    2 * 3 > 4
    2 * (3 > 4)
    2 * (4 > 3)

# 4. Combining lists

Calculate all coordinates of the line x=y with x < 100.
- **Note**: This is the sequence (0, 0), (1, 1), ... (99, 99)

# 5. Dictionaries

We are going to store the output of a function (f(x)=x2) together with its input in a dictionary.
- Make a dictionary containing all squares smaller than 100.
- Print the content of this dictionary in english, e.g., "4 is the square of 2".

# 6. k-mer counting

## (1/2)

Remember the previous exercise of finding (unique) substrings of length 3.
- Make a function from your implementation.
- Have *k* as an argument to the function.
- Test the function on several input strings.

## (2/2)

Modify your function to use a dictionary with substring counts.
- Use the substrings as dictionary keys.
- Use the counts as dictionary values.
- Have the function return the dictionary.
- Add a docstring to the function.
- Use the function to print k-mer counts for some strings.

# 7.FizzBuzz

Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
