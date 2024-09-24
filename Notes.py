'''
	File Name: Errors
	Author: Mr. Kalisz
	Date Created: Sept 24, 2024
	Date Last Edited: Sept 24, 2024
'''

print(5)

#Errors

#Syntax Errors - Errors cauased by not following the rules of your programming language
#Syntax Errors always happen before the code runs

#num = 3 = 5
'''
File "/workspaces/ics2o1-01-24-25-practice-problem-1-6-PP1.6-ICD2O/Notes.py", line 14
    num = 3 = 5
          ^
SyntaxError: cannot assign to literal
'''

#num = (3 + (5 - 4) * 5
'''
  File "/workspaces/ics2o1-01-24-25-practice-problem-1-6-PP1.6-ICD2O/Notes.py", line 22
    num = (3 + (5 - 4) * 5
          ^
SyntaxError: '(' was never closed
'''

#Runtime Errors - Errors that happen based on a value - won't always happen
#Errors happen while your code is running

#print(5 / 0)
'''
  File "/workspaces/ics2o1-01-24-25-practice-problem-1-6-PP1.6-ICD2O/Notes.py", line 34, in <module>
    print(5 / 0)
          ~~^~~
ZeroDivisionError: division by zero
'''
#print(3 + "word")
'''
  File "/workspaces/ics2o1-01-24-25-practice-problem-1-6-PP1.6-ICD2O/Notes.py", line 41, in <module>
    print(3 + "word")
          ~~^~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

#Logical Errors - Program executes flawlessly but with the wrong outcome
#Error that happens after our program - based on the result
#There is no error message, you need to use your output to check

#Add 3 and 5 together

print(3 + 5) #Instructions don't say to output it

#Add 2 and 2 together, out the result

print(1 + 2) #Wrong values

#Add 3 and 5 together then multiply by 2, output the result

print(3 + 5 * 2) #Order of operations

#Add 2 and 2 together then multiply by 1, then output it

print(2 + 2 * 1) #Order of operations, but the result is correct.  This does not mean the program is
