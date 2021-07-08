# Custom Eval Module

## Problem Statement:
- You are given a string expression with operands (numbers) and operators
(addition, subtraction, multiplication & division) separated by spaces.
Assume there will be no brackets. Your goal is to write a program to output
the final value of the evaluated expression. Given below are a few
examples:

```
input:"30 + 6 - 2 + 8"
output: 42

input: "55 - 13 + 5 - 12"
output: 35

input: "12 - 3 * 6"
output: -6

input: "9 * 2 - 8 / 4 + 5"
output: 21
```

- Constraints: 
    - The length of the string can be arbitrarily large but you can safely assume that it will fit in the available program memory.
    - You are not allowed to use inbuilt expression evaluation functions (ex. eval() in python)


<br/>

## Solution:
- Run from root directory of this project
```
#input from input file
python3 src/code/main.py input.txt

#input as string expression
python3 src/code/main.py "1 + 2 - 4 / 2"
```