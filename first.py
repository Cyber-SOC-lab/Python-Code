#!/bin/python3

print("Hello World!")
print('Hello world')
print("""this is a string runs
mutiple lines!""") #triple quote for mutli-line
print("This is a combine "+"string ")
print('\n')
print("Testing the new line special sequences")


print('\n')
#MATH

print(50 + 50) #ADD
print(50 - 50) #sub
print(50 * 50) #Multi
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponent
print(50 % 6) #module - take what is left over
print(50 / 6)
print(50 // 6)

print('\n')
#VARIABLE AND METHODS

quote= "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case

name= 'Bilal' #string
age= '20'
gpa= '3.1'

print(int(age))
print(int(30.1))

print("My name is " + name + " and I am " + str(age) + " years old.")


print('\n')
#FUNTIONS

def my_func(): #funtion wihout parameters
	name = "Bilal" #Local variable
	age = 20
	print("My name is " + name + " and I am " + str(age) + " years old.")
	
my_func()

def add_one_hundred(num):
	print(num + 50)

add_one_hundred(100)

def value(bilal,Rajput):
	print(bilal + Rajput)
	
value(2,7)

def multi(x,y):
	return x * y
	
multi(8,8)
print(multi(8,8))

def square_root(x):
	print(x ** .1)
	
square_root(60)	

def nl():
	print('\n')
	
nl()

#Boolean Expression (True or False)

bool1 = True
boot2 = 3*3 == 9
bool3 = False 
bool4 = 3*3 != 6

print(bool1,boot2,bool3,bool4)
print(type(bool1))

bool5 ="True"
print(type(bool5))

nl()
#Relational And Boolean Operators
greater_than =7 > 5
les_than = 5 < 7
greater_than_equal_to = 7>=6
less_than_equal_to = 7<=7

test_and = (7 > 5) and (5 < 7) #true
test_and2 = (7 > 5) and (5 > 7) #false		
test_or = (7 > 5) or (5 < 7) #true
test_or = (7 > 5) or (5 > 7) #false

test_not = not True #false
test_not = not False #true

nl()
#Conditional Statements

def exam(attendence):
	if attendence >= 75:
		return " Congrats You're eligible to give exams"
		
	else:
	      	return " Sorry, You're not eligible to sit in exams"
	
print(exam(79))
print(exam(65))

nl()

age = input("Please enter your age: ")
marks = input(" What's the results of your test marks: ")
	
if (age == 18) and (marks >= 5):
	print( " Congrats you're allowed to get your license!")
		
elif (age != 18) and (marks == 10):
	print(" You're under age kid!")
	
elif (age == 18) and (marks != 5 ):
	print(" Sorry, please try again later")
		
else:
       	print(" Sorry please enter valid details")
		
		
	
			 	      	
	      			
