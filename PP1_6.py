'''
	File Name: errors.py
	Author: Mr. Kalisz
	Date Created: March 29, 2019
	Date Last Edited: Sept 23, 2024
'''

# From input, recieve two integers from the user and add them together.  Output the result.
def q1():
  num1 = float(input("Input a number: "))
  num2 = float(input("Input a number: "))
  
  print(float(num1 + num2))

# From input recieve two integers.  Output the quotient rounded down.

def q2():
  num1 = float(input("Input a number: "))
  num2 = float(input("Input a number: "))  
  print(int(num1 / num2))

# Output the phrase "hello Mr. Kalisz have you seen my work yet?"

def q3():
  print ("hello Mr. Kalisz have you seen my work yet?")

# From input recieve two numbers (can be decimal fractions).  
# Output their result multiplied together.  Then round down to the nearest whole number

def q4():
  num1 = float(input("Input a number: "))
  num2 = float(input("Input a number: "))
  print (int(num1 * num2))

#q1()
#q2()
#q3()
#q4()