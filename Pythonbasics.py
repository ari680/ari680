#!/usr/bin/env python
# coding: utf-8

# ## Why Python?
# Python is very beginner-friendly. The syntax (words and structure) is extremely simple to read and follow, most of which can be understood even if you do not know any programming
# 
# 
# <ul>-Readable</ul>
# <ul>-Dynamic</ul>
# <ul>-Fast</ul>
# <ul>-Poweful</ul>
# 
# 

# In[1]:


from IPython.display import Image
from PIL import Image


# <h3>Python Version</h3>
# 
# 1. python - 2.0
# 2. python - 3.0

# <h3>What is Python</h3>

# Multipurpose programming language(Web, GUI, Scripting etc)<br>
# Object Oriented

# <h3>Who Invented</h3>
# 
# Python was conceived in the late 1980s, and its implementation began in December 1989 by <b>Guido van Rossum</b> at Centrum Wiskunde & Informatica (CWI) in the Netherlands 

# In[ ]:


display(Image.open(path + '/python_inv.jpg'))


# <h3>Companies Using Python</h3>

# In[ ]:


display(Image.open(path + '/comp_python.png'))


# ## Python Basic Installation
# 
# https://www.python.org/downloads/
# 
# https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html

# <h3>Conda Installation</h3>
# 
# Conda is an opensource package management system and environment management system that runs on windows, macOS and Linux. Conda quikly installs, runs and updates packages and their dependies.
# 
# https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444
# 
# For Mac
# https://conda.io/docs/user-guide/install/macos.html
# 
# 
# To Install Anaconda/MacOS/ follow this link
# https://medium.com/@GalarnykMichael/setting-up-pycharm-with-anaconda-plus-installing-packages-windows-mac-db2b158bd8c

# <h3>Python IDE</h3>
# 
# An integrated development environment (IDE) is a software suite that consolidates the basic tools developers need to write and test software. Typically, an IDE contains a code editor, a compiler or interpreter and a debugger that the developer accesses through a single graphical user interface (GUI).<br>
# 
# #for MAc
# https://www.jetbrains.com/pycharm-edu/download/#section=mac
# 
# #for Windows
# https://www.jetbrains.com/pycharm-edu/download/#section=windows
# 
# #for Linux
# https://anaconda.org/chen/pycharm

# In[ ]:


display(Image.open(path + '/ide.png'))


# ## Python - Print Function
# 
# The print function in Python is a function that outputs to your console window whatever you say you want to print out. 
# This is a great tool for debugging
# "Debugging" is the term given to the act of finding, removing, and fixing errors and mistakes within code.
# 

# In[ ]:


#python 3.5
print("Hello world")
print(5)

#python 2.7
#print "Hello World"

#print(“single quotes”)
#print(‘double quotes’)
#You can use single quotes or double quotes, 
#but they need to be used together


# In[ ]:


get_ipython().run_line_magic('pinfo', 'print')


# ## Python - String
# Strings are a type of data - text or sequence of characters
# 

# In[ ]:


#String
#int
#float
#Boolean


# In[ ]:


"Hello World"
'Welcome to the python basic tutorial'
print("Hello World")


# ## Python - Int, Float

# In[ ]:


#To declare Integer
2
print(2)

#To declare Float
2.5
print(2.5)

#To declare Boolean
True
False
print(True)
print(False)


# ## Python - Concatenation
# Concatenation is combining string with string or string with number or number with number
# 
# You can use either + or , to join together
# If you use the "+" to join integers and floats together, then you will perform an arithmetic operation
# If you use the ",", then it will print them out separately, with a space.

# In[ ]:


f_name = "peter"
l_name = "Loyd"
Age = 25

#String, String
full_name = print(f_name, l_name)
full_name2 = print(f_name + l_name)
my_age = print(full_name, Age)


# In[ ]:


#string vs string
print("Hello" + "world")
print("Hello", "world")
print("age", 25)
print(5,5)


# ## Python - Maths Basics
# 
# Math is a pretty popular topic, so we should probably learn how to do it in Python 3. Luckily for us, math is so very 
# popular that it works extremely simply.
# 

# In[ ]:


1 + 3
4 * 4
5 - 2
5 / 2
4 ** 2 
"Hi" * 5

A = 1
B = 3
print(A + B)
print(4 ** 4)


# In[ ]:


#string multiplication
print('hi'*2)


# In[ ]:


#modulus - returns reminder value
print(3%2)


# ## Python - Variables
# 
# Variables act as placeholders for data. Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory
# 

# ### Assign Value to Variables
# Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.
# 
# The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable

# In[ ]:


name = "ms.Buck"
age = 25
likes = "chocklate"

#name, age, likes are variables
#"ms.Buck", 25, "chocklate" are vales belongs to variable

#Multiple Assignments
a = b = c = d = 5
print(a)
print(b)
print(c)
print(d)


# In[ ]:


#Variable should be unique
#It should not start with number
#There should not be space between variable names 
#(My Name should be My_Name or MyName)


# # Data Structure

# Data structures are basically the particular way of organizing data. In other words, they are used to store a collection of related data.
# There are four built-in data structures in Python 
# 1. list 
# 2. tuple 
# 3. dictionary
# 4. set 
# 
# We will see how to use each of them and how they make life easier for us.

# ## Python List

# A list is a data structure that holds an ordered collection of items i.e. you can store a sequence of items in a list,
# A Python list acts very much like an array

# In[ ]:


#lists are ordered collection of items - index
#mutable
#[]

x = [1,3,5,6,2,1,6]
print(x)


# In[ ]:


x = [1,3,5,6,2,1,6]
print(x)

print(x[0],x[1])

sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']

#When we print out the list, the output looks 
#exactly like the list we created

print(sea_creatures)
#['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']

#positive Indexing - left - write
#0 - n == 0, 1, 2, 3,4
#Negative Indexing - rite - left
#-1. == -5 -4 -3 -2 -1


# #### Indexing lists
# 
# Each item in a list corresponds to an index number, which is an integer value, starting with the index number 0.
# For the list sea_creatures, the index breakdown looks like this:
# 
# 'Shark'' - 0 “Cuttlefish' - 1 “'Squid' - 2 ‘'mantis shrimp'' - 3 “Anemone' - 4
# 
# Now we can call a discrete item of the list by referring to its index number:
# 

# In[ ]:


print(sea_creatures[1])


# #### Task: Call all the items individually in the following order
# "Shark”
# “Cuttlefish”
# “Squid”
# "mantis shrimp"
# “Anemone”
# 

# <h3>For the same list sea_creatures, the negative index breakdown looks like this:</h3>
# 
# 'Shark'' - (-5)“Cuttlefish' - (-4)“'Squid' - (-3) ‘'mantis shrimp'' - (-2)“Anemone' - (-1)
# 

# In[ ]:


print(sea_creatures[-2])


# ### Slicing Lists

# In[ ]:


"""With slices, we can call multiple values by 
creating a range of index 
numbers separated by a colon 
"""
print(sea_creatures[1:4])

"""When creating a slice, as in [1:4], 
the first index number is where the slice starts (inclusive), and the second index number is where the slice ends (exclusive), 
which is why in our example above the items at position, 1, 2, and 3 are the items that print out
"""
#This printed the beginning of the list, 
#stopping right before index 3.

print(sea_creatures[:3])
['shark', 'octopus', 'blobfish']

#To include all the items at the end of a list, 
#we would reverse the syntax:

print(sea_creatures[2:])

#We can also use negative index numbers when slicing lists,
#just like with positive index numbers:

print(sea_creatures[-4:-2])
print(sea_creatures[-3:])


# ### List Manipulation

# In[ ]:


#Here is some example code of list manipulation:
#We can add, remove, count, sort, search, and do 
#quite a few other things to python lists.

x = [1,6,3,2,6,1,2,6,7]
x.append(55)
print(x)

"""What if you have an exact place that you'd like to put something in a list, 
instead of just at the very end?
"""
x.insert(2,33)
print(x)

#Now delete the value based on index number
del (x[2])
print(x)

#To check total number of values in the list
print(len(x))

#To get to know the occurence of each element
from collections import Counter
print(Counter(x))



#Next, remember how we can reference an item by index in a list? Like:
print(x[5])


#sorting
x.sort()
print(x)

#For descending
print(x.sort(reverse=True))

#For Ascending
print(x.sort(reverse=False))

#What if these were strings? like:

y = ['Jan','Dan','Bob','Alice','Jon','Jack']

y.sort()
print(y)

y.reverse()
print(y)


# In[ ]:


x.insert(3, 45)


# In[ ]:


print(x)


# In[ ]:


del (x[4])


# In[ ]:


print(x)


# In[ ]:


print(len(x))


# In[ ]:


x.sort()


# In[ ]:


print(x)


# In[ ]:


x.sort(reverse=True)


# In[ ]:


print(x)


# In[ ]:


from collections import Counter
print(Counter(x))


# ### Multi Dimensional list

# In[1]:


#Multi dimensional lists are lists within lists, 
#or lists within lists within lists.

X = [ [2, 6], [6, 2], [8,4], [5, 12] ]
print (X)

#We can also take this deeper since we have more dimensions now:

print(X[2][1])


# <b>Example</b>

# In[ ]:


fruits = [["Apple", "Red"], ["Orange", "Orange"], 
          ["Banana", "Yellow"], ["Grape", "Black"]]
print(fruits)


# In[ ]:


fruits[0]


# In[ ]:


fruits[0][1]


# In[ ]:


fruits[0][1], fruits[1][1], fruits[2][1]


# In[ ]:


fruits[0][1] = "Green"


# In[ ]:


print(fruits)


# In[ ]:


del fruits[0][1]


# In[ ]:


print(fruits)


# In[ ]:


fruits[-1][1] = 'Green'


# In[ ]:


print(fruits)


# In[ ]:


fruits = [[ ["Apple", "red"], ["Orange", "orange"] ]]


# ## Python - Dictionaries
# Dictionaries are a data structure in Python that are very similar to associative arrays. They are non-ordered and contain "keys" and "values." Each key is unique and the values can be just about anything, but usually they are string, int, or float, or a list of these things. Dictionaries are defined with {} curly braces.
# 
# Use {} curly brackets to construct the dictionary, and [] square brackets to index it. Separate the key and value with colons : and with commas , between each pair. Keys must be quoted As with lists we can print out the dictionary by printing the reference to it. A dictionary maps a set of objects (keys) to another set of objects (values)
# 
# Dictionaries are mutable and unordered DataStructures

# In[ ]:



exDict = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}
print(exDict)

#How old is Jack?
print("the age of jack is", exDict['Jack'])

#We find a new person that we want to insert:
exDict['Tim'] = 14
print(exDict)

#Tim just had a birthday though!
exDict['Tim'] = 15
print(exDict)

#Then Tim died.
del exDict['Tim']
print(exDict)


# In[ ]:


exDict = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}
print(exDict)


# In[ ]:


exDict.keys()


# In[ ]:


#Next We want Track Hair Color
exDict={'Jack':[15,'blonde'],'Bob':[22,'brown'],
        'Alice':[12,'black'],'Kevin':[17,'red']}
#print(exDict['Jack'][1])


# In[ ]:


print(exDict)


# In[ ]:


print(exDict['Jack'][0], exDict['Bob'][1])


# <b>Example</b>

# In[ ]:


c = {"Apple": "Red", "Orange": "Orange", "Banana": "Yellow"}


# In[ ]:


c["Apple"]


# In[ ]:


c["strawberry"] = "Red"


# In[ ]:


print(c)


# In[ ]:


del c["strawberry"]


# In[ ]:


print(c)


# In[ ]:


len(c)


# In[ ]:


fruits = {"Apple": ["Red", "round"], 
          "Orange": ["Orange", "round"], 
          "Banana": ["Yellow", "hook"]}


# In[ ]:


fruits["Apple"][1]


# ### MultiDimensional Dictionary

# In[ ]:


fruits = {"fruits_name":{
    "Apple":{
        "color":"red",
        "Shape": "round"
        
    },
    
    "Orange":{
        "color":"Orange",
        "Shape": "round"
    }
}}


# In[ ]:


print(fruits)


# In[ ]:


fruits["fruits_name"]


# In[ ]:


fruits["fruits_name"]["Apple"]


# ## Python Tuples
# A Tuple is a dataset that similar to lists. but a tuple is fundamentally different in that a tuple is "immutable." This means that it cannot be changed, modified, or manipulated. A tuple is typically used specifically because of this property. A popular use for this is sequence unpacking, where we want to store returned data to some specified variables. Something like:

# In[ ]:


# Tuples also can have curved brackets like "(" or ")"

sub = ('physics', 'chemistry', 1997, 2000)
id = (1, 2, 3, 4, 5 )
alph = ("a", "b", "c", "d")


# In[ ]:


print(sub)


# In[ ]:


print(sub[0])


# In[ ]:


#Tuples are immutable(Cannot be modified)
#Following action is invalid
#'tuple' object does not support item assignment - 
#Hence tuple doesen't support mutation


sub[0] = 'Maths'


# In[ ]:


#deletion
#tuple' object doesn't support item deletion
del sub[0]


# In[ ]:





# ## Python Sets
# Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
# 
# Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure that we discuss in the next section.

# In[ ]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket) 


# In[4]:


fruit = set('datascience')
fruit


# This shows that duplicates have been removed

# # Control Flow<br>
# 
# In the programs we have seen till now, there has always been a series of statements faithfully executed by Python in exact top-down order. What if you wanted to change the flow of how it works? For example, you want the program to take some decisions and do different things depending on different situations, such as printing 'Good Morning' or 'Good Evening' depending on the time of the day?
# As you might have guessed, this is achieved using control flow statements. There are three control flow statements in Python - 
# 1. if  
# 2. for
# 3. while.
# 

# ## Loops
# 
# Loops - Statements are executed sequentially
# 
# The two distinctive loops we have in Python 3 logic are the "for loop" and the "while loop." Both of them achieve very similar results, and can almost always be used interchangeably towards a goal. 
# Generally, the for loop can be more efficient than the while loop, but not always.
# 

# ## Python While Loop
# 
# While loop Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.  This repeats until the condition/expression becomes false.
# 
# 

# In[ ]:


import time
number = 1
while number < 10:
    print(number)
    number += 0 #number = number + 1
    time.sleep(1)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'time')


# Next, we specify the terms of the while statement, which are : While the number variable is less than 10, we will print the number variable out. After printing out the number, we will add 1 to the number.
# This process will continue until condition equals 10.

# """print(condition)
#     condition += 1
# """
# 
# This setup of a while loop is known as creating a "counter," since basically that is what we're doing. We're saying we just want to count 1 for every iteration and eventually stop at our limit. While loops are usually finite and defined in this sense, but while loops can also be undefined. Something like
# 

# In[ ]:


x = 'mango'
while x == 'mango':
  
  print("the output is mango")
  x = 'orange'


# In[ ]:


### Infinite while loops

"""An infinite loop (sometimes called an endless loop ) 
is a piece of coding that lacks a functional exit so that it repeats indefinitely
"""
"""number = 1
while number < 10:
    print(number)"""


# In[ ]:


### While Else Loop


number = 1
while number < 5:
    number += 1 #number = number + 1
    time.sleep(1)
    print(number)
else:
    print("count is not lessthan 5")    


# In[ ]:


### Single Statement loops

flag = True
while (flag):  # While flag True
    print ('Given flag is really true!')
    
    flag = False #To Brak loop flag become False
    
print ("Good bye!")


# <b>Examples1</b>

# In[ ]:


#Stop loop with break
#break function stops loop
#It avoids Infnite looping

name = "Robert"
while name == "Robert":
    print(name)
    age = 25
    salary = 20000
    bonus = 20000*0.2
    total_salary = salary + bonus
    print(name, salary, age, bonus, total_salary)
    break


# <b>Examples2</b>

# In[ ]:


#Stoping loop by making Condition False
#Here condition become false
#by changing value in name
name = "Robert"
while name == "Robert":
    print(name)
    age = 25
    salary = 20000
    bonus = 20000*0.2
    total_salary = salary + bonus
    print(name, salary, age)
    name = "James"
    print(name)


# <b>Examples 3</b>

# In[ ]:


#While Else loop
#While Condition True
#block of code under while execute
#while condition False
#block of code under Else Executes

name = "Robert"
while name == "Robert":
    age = 25
    salary = 20000
    bonus = 20000*0.2
    total_salary = salary + bonus
    print(name, salary, age)
    #making condition False
    name = "James"
    print(name)
    
else:
    print("Name is not robert")


# In[ ]:


x = True
y = True
while x:
  print("X value is True")
  while y:
    print("Y value is True")
    break
  break


# In[ ]:


#Applying While Loop for list of Elements

names = ["robert", "james", "mary", "rachell"]

output_names = []
while "robert" in names: #true
    i = 0
    while i < len(names):
        print(names[i])  #list slicing names[1], names[2] etc
        #iteration method
        names_i = names[i]
        output_names.append(names_i)
        i+=1 #i = i + 1
    break
else:
    print("Every thing is fine")

print(output_names)
    


# In[ ]:


print(len(names))


# ## Python For Loop
# 
# It iterates over a sequence of object and go through each item in a sequence. Sequence is just an ordered collection of items
# 
# For Loop, Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.
# The next loop is the For loop. The idea of the for loop is to "iterate" through something. For each thing in that something, it will do a block of code. Most often, you will see a for loop's structure very much like this.

# In[ ]:


"""for eachThing in thisThing:
    do this stuff
    in this block"""
fruits = ['apple', 'mango', 'banana']
for fruit in fruits:
  print(fruit)
  break


# In[ ]:


#This code will print out each item in that list.

exampleList = [1,5,6,6,2,1,5,2,1,4]

for x in exampleList:
    print(x)
    time.sleep(1)


# This code is actually what is known as a generator function, and is highly efficient. The above works very much like the "counter" function we made with a while loop. The only difference is this one is much faster and more efficient in many cases.

# In[ ]:


for x in range(1,11):
    print(x)


# In[ ]:


names = ["robert", "james", "mary", "rachell"]

#For loop exits after last value in list
#n is new variable to store every iterated next element

for n in names:
    print(n)
print("Every thing is fine")


# ### Nested For Loop
# This code actually prints the tables from 1 to 10. Where in loop x runs one time then loop, Y runs till the loop ends. X and Y values stores in the respective variable
# X = 1 Y=1
# X=1 Y=2
# Etc for the 1st Main loop

# In[ ]:


for x in range(1, 3):
    for y in range(1, 3):
        print ('%d * %d = %d' % (x, y, x*y))
        


# %s is used as a placeholder for string values you want inject into a formatted string
# %d is used as a placeholder for numeric or decimal values.

# ## Conditional Statement
# Conditional statements are part of every programming language. With conditional statements, we can have code that sometimes runs and at other times does not run, depending on the conditions of the program at that time

# ## Python IF Statement
# The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block).

# Here, we define the variables x and y. Then, we ask if x is greater than y. If it is, then we will print 'x is greater than y.' If it is not, then nothing will happen.
# 

# In[ ]:


x = 5
y = 10

#if condition:
  
if x > y:  #flase
    print('x is greater than y')

#In this case, 5 is not greater than 10, so nothing will happen.


# In[ ]:


#Now we have flipped the comparison operator to say if x is less than y

x = 5
y = 10

if x < y: #true
    print('x is less than y')


# In[ ]:


#example: 1

balance = -5

if balance < 0: #True
    print("Balance is below 0, add funds now or you will be charged a penalty.")


# In[ ]:


#example 2

grade = 60

if grade <= 65: #True
    print("Failing grade")


# In[ ]:


if
if elif 
if else
if elif else


# ### More Conditional Expressions

# In[ ]:


display(Image.open(path + '/if.png'))
#<img src='if.png'/>


# ### If else statement
# 
# It is likely that we will want the program to do something even when an if statement evaluates to false. 
# 
# The If-Else statement is designed to build on the if statement logic. Here, we ask if something is the case, and, if it is we do something. Then we say otherwise, which is contingent on the previous if statement, do something else. If the previous if statement is true, then the else will not run. If the if statement is false, then the else statement will run.
# 

# In[ ]:


#So first we ask if x is greater than 55. 
#It is not, therefore the else statement runs.

x = 5
y = 8
if x > 55: #False
    print('x is greater than 55')
else: #print
    print('x is not greater than 55')


# In[ ]:


#If we instead do ask for x is less than 55 
#then else statement does not run

x = 5
y = 8
if x < 55: #True
    print('x is less than 55')
else:
    print('x is not less than 55')


# In[ ]:


#example -1
grade = 60

if grade >= 65: #False
    print("Passing grade")

else:
    print("Failing grade")


# In[ ]:


#example -2
balance = 522

if balance < 0: #False
    print("Balance is below 0, add funds .")

else:
    print("Your balance is 0 or above.")


# ### if Elif Else statement
# 
# So far, we have presented a Boolean option for conditional statements, with each if statement evaluating to either true or false. In many cases, we will want a program that evaluates more than two possible outcomes. For this, we will use an else if statement, which is written in Python as elif. The elif or else if statement looks like the if statement and will evaluate another condition.
# 
# 
# Now we bring the in "elif" statement. The elif allows us to tie multiple if statements together as we might have intended to before with multiple if statements before we learned that the else will only be contingent on the if statement above it.

# In[ ]:


x = 5
y = 10
z = 22

if x > y: #False
    print('x is greater than y')
elif x < z: #True
    print('x is less than z')
else:
    print('if and elif never ran...')


# Here, we ask if x is greater than y first. 5 is not greater than 10, so this is False. So the elif runs to ask if x is less than z. In this case, it is asking if 5 is less than 22. It is, so we will see a print out saying x is less than z. The "else" part of this will not run.

# In[ ]:


x = 5
y = 10
z = 22

if x > y: #False
    print('x is greater than y')
elif x > z: #False
    print('x is greater than z')
else:
    print('if and elif never ran...')


# Here, we ask if x is greater than y first. 5 is not greater than 10, so this is False. So the elif runs to ask if x is greater than z. In this case, it is asking if 5 is greater than 22. This is false, so it does not run. Then, we find ourselves at the else statement, which notifies us that 'if and elif never ran...'

# In[ ]:


#Example - 1

grade = 75

if grade >= 90: #False
    print("A grade")

elif grade >=80: #False
    print("B grade")

elif grade >=70: #True
    print("C grade")

elif grade >= 65:
    print("D grade")

else:
    print("Failing grade")


# <h3>Example</h3>

# In[ ]:


#If Condition
balance = 10000
penalty = 0.2

if balance <= 10000: #True
    """
    args: penality
    10000*0.2
    """
    penalty = balance *0.2
    balance = balance - penalty
    print(penalty, balance)


# In[ ]:


#if vs else
balance = 10000
penalty = 0.2

if balance < 10000: #False
    penalty = balance *0.2
    balance = balance - penalty
    print(penalty, balance)
else:
    print("You have minimum balance in your account")
    interest_rate = 0.06
    interest = balance * interest_rate
    balance = balance + interest 
    #balance += interest
    print(interest_rate, interest, balance)
    #print("Your interest_rate is {}, interest_amount is {}, 
    #balance is {}".format(interest_rate, interest, balance ))


# In[ ]:


#if-elif-else

balance = 11000
penalty_0 = 0.2
penalty_1 = 0.1

if balance <= 10000: #False
    penalty = balance *penalty_0
    balance = balance - penalty
    print(penalty, balance)
    
elif balance > 5000 and balance < 8000: #False
    penalty = balance *penalty_1
    balance = balance - penalty 
    print(penalty, balance)
    
elif balance > 8000 and balance <= 11000: #True
    penalty = balance *penalty_1 * 2 
    balance = balance - penalty 
    print(penalty, balance)
    
    
else:
    print("You have minimum balance in your account")
    interest_rate = 0.06
    interest = balance * interest_rate
    balance += interest #(balance = balance + interest)
    print("Your interest_rate is {}, interest_amount is {}, balance is {}".format(interest_rate, interest, balance ))


# In[ ]:


#if-elif-else

balance = 11000
penalty = 0.2
penalty_1 = 0.1

if balance <= 10000: #False
    penalty = balance *0.2
    balance = balance - penalty
    print(penalty, balance)
    
elif balance > 5000 and balance < 8000: #True
    penalty = balance *penalty_1
    balance = balance - penalty 
    print(penalty, balance)
    
elif balance > 8000 and balance <= 11000:
    penalty = balance *penalty_1 * 2 
    print(penalty_1*2)
    balance = balance - penalty 
    print(penalty, balance)
    
    
else:
    print("You have minimum balance in your account")
    interest_rate = 0.06
    interest = balance * interest_rate
    balance += interest
    
    print("Your interest_rate is {}, interest_amount is {}, balance is {}".format(interest_rate, interest, balance ))


# In[ ]:


balance = 11000
penalty = 0.2
penalty_1 = 0.1

#range
if balance > 10000 and balance <15000:
    penalty = balance*0.02
    balance = balance - penalty
    print(penalty, balance)
    
elif balance <10000 and balance >5000:
    penalty = balance*0.03
    balance = balance + penalty
    print(penalty, balance)
    
else:
    print("You have sufficient balance")
    


# ### Nested IF statementt
# We can use nested if statements for situations where we want to check for a secondary condition if the first condition executes as true. For this, we can have an if-else statement inside of another if-else statement. Let’s look at the syntax of a nested if statement

# In[ ]:


statement1 = True
nested_statement = False

if statement1: #False
    print("true")
    
    if nested_statement:
        print("yes")
        
    else:
        print("no")
        
else:
    print("false")


# In[ ]:


#We also can have  multiple if statement
grade = 85

if grade >= 65: #True
    print("Passing Grade of:")
    
    if grade >= 90: #False
        print("A")
        
    elif grade >= 80: #True
        print("B")
        
    elif grade >= 70:
        print("C")
        
    elif grade >= 65:
        print("D")
        
else:
    print("Failing Grade")


# In[ ]:


#Even we want to evaluate grades like A+, B+ etc
grade = 85

if grade >= 65: #true
    print("Passing Grade of:")
    
    if grade >= 90: #false
        print("A")
        
        if grade <= 92:
            print("Your Grade is :", "A+")
        elif grade > 92 and grade <= 95:
            print("Your Grade is :", "A++")
        else:
            print("Your Grade is :", "A+++")
            
        
    elif grade >= 80: #true
        print("B")
        
        if grade <= 82: #false
            print("Your Grade is :", "B+")
        elif grade > 82 and grade <= 85: #true
            print("Your Grade is :", "B++")
        else:
            print("Your Grade is :", "B+++")
        
    elif grade >= 70:
        print("C")
        
        if grade <= 72:
            print("Your Grade is :", "C+")
        elif grade > 72 and grade <= 75:
            print("Your Grade is :", "C++")
        else:
            print("Your Grade is :", "C+++")
        
    elif grade >= 65:
        print("D")
        
        if grade <= 62:
            print("Your Grade is :", "D+")
        elif grade > 62 and grade <=65:
            print("Your Grade is :", "D++")
        else:
            print("Your Grade is :", "D+++")
        
else:
    print("Failing Grade")


# <h3>Example</h3>

# In[ ]:


balance = 10000
penalty = 0.2
penalty_1 = 0.1

if balance <= 10000:
    penalty = balance *0.2
    balance = balance - penalty
    print(penalty, balance)
    if balance >=8000 and balance <=8999:
        gst_rate = 0.18
        gst_charges = balance*gst_rate
        balance -= gst_charges
        print(gst_rate, gst_charges, balance)
        #print("Your gst_rate is {}, gst_charges is {}, 
        #balance is {}".format(gst_rate, gst_charges, balance))
        
        if gst_rate == 0.18:
            print("This tax slab from India")
        else:
            print("This tax slab is not from india")
                  
elif balance > 5000:
    penalty = balance *penalty_1
    balance = balance - penalty
    print(penalty, balance)
    
else:
    print("You have minimum balance in your account")
    interest_rate = 0.06
    interest = balance * interest_rate
    balance += interest
    print(interest_rate, interest, balance)
    #print("Your interest_rate is {}, interest_amount is {}, 
    #balance is {}".format(interest_rate, interest, balance ))


# ## Python Functions
# 
# A function is a block of organized, reusable code that is used to perform a single, related action
# The idea of a function is to assign a set of code, and possibly variables, known as parameters, to a single bit of text

# ### Defining Function
# Function blocks begin with the keyword <b>def</b> followed by the function name and parentheses ( ( ) ). And also choose unique function name
# 
# Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses
# 
# The code block within every function starts with a colon (:) and is indented
# 
# The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

# In[ ]:


def calculate_num():
  x = 24
  multiple_x = x ** 2
  print(multiple_x)


# In[ ]:


calculate_num()


# In[ ]:


X = 8
Y = 9
Z = 8 + 9
print(Z)


# it a lot like why you choose to write and save a program, rather than writing out the entire program every time you want to execute it.

# In[ ]:


def my_add(X, Y):
    Z = X + Y
    print(Z)


# ### Calling a Function
# Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code.

# In[ ]:


my_add(1, 3)


# In[ ]:


def create_sum():
    print('this code will run')
    z = 3 + 9
    print(z)


# Now if we just run this, we see nothing happens. We have to actually call this function to execute, because all we've done so far is just define the function and what it does. To run it, you can either type out the function in the console like so:

# In[ ]:


create_sum()


# In[ ]:


#example: 1 

def addme(my_list):
    my_list.append([1, 2, 3, 4])
    print("Values inside a function", my_list)
    return

my_list = [23, 25, 26, 28]
addme(my_list)
    


# ### Functions Parameters
# 
# The term parameter (sometimes called formal parameter) is often used to refer to the variable as found in the function definition, while argument (sometimes called actual parameter) refers to the actual input supplied at function call
# 
# The idea of function parameters in Python is to allow a programmer who is using that function, define variables dynamically within that function. For example:

# In[ ]:


def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)
    
simple_addition(5,3)


# In[ ]:


def simple_addition(x, y):
  z = x + y
  print(z)


# In[ ]:


simple_addition(x=10, y=11)


# In[ ]:


x = 10
y = 11
simple_addition(x, y)


# In[ ]:


simple_addition(14, 15)


# In[ ]:


#hardcoded

def calculate_sum():
  x = 10
  y = 12
  z = x + y
  print(z)


# In[ ]:


calculate_sum()


# #### Keyword Arguments
# 
# Keyword argumnet is the in a function call, the caller identifies the argument by its parameter

# In[ ]:


"""If you have a lot of parameters where it might be difficult 
to remember their order, you could do something like:
"""
simple_addition(num2=3,num1=5)


# In[ ]:


# Function definition is here
def my_data( name, age ):
   "This prints a passed info into this function"
    print ("Name: ", name)
    print ("Age ", age)
    return;

# Now you can call printinfo function
my_data( age=50, name="sonu" )


# ### Functions Parameters Defaults
# 
# A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.
# 
# we have function parameter defaults, which allow the function's creator to set "default" values to the function parameters. This allows anyone to use a function with the default values, yet lets anyone who wishes to customize them the ability to specify different values.

# In[ ]:


def simple(num1, num2=5):
    Pass


# This is just a simple definition of a function, with num1 not being pre-defined (not given a default), and num2 being given a default.

# In[ ]:


color = ["red", "black"]
model = ["sports", "luxury"]


def car(color, model, brand="Ferrari"):
    for c in color:
        print("color :", c)
        if c == "red":
            model1 = model[0]
            print(brand, c, model1)
        else:
            print(brand, color[1], model[1])
    print("Selecting the car")


# In[ ]:


car(color, model, brand="Benz")


# In[ ]:


def basic_window(width, height, font='TNR'):
    # let us just print out everything
    print(width,height,font)
basic_window(350,500)


# In[ ]:


"""Here's another example, only this time we see that, 
despite the parameter having 
a default, we are able to still change it.
"""
basic_window(350,500,font='courier')


# In[ ]:


#More parameters or less parameters will not give any output
#This will not work:

def simple_addition(x, y):
  print(x, y)

#simple_addition(3,5,6)

#nor will this:

simple_addition(3)


# <h3>Example</h3>

# In[ ]:


def cars(car_list):
    for name in car_list:
        if name == "Benz": #true
            color_car = "black"
            model_car = "Luxury"
            price = "$20000"
            print(name, color_car, model_car, price)

        elif name == "Ferrari":
            color_car = "red"
            model_car = "Sports"
            price = "$40000"
            
            print(name, color_car, model_car, price)
            
        elif name == "BMW":
            color_car = "White"
            model_car = "Semi sports"
            price = "$30000"
            
            print(name, color_car, model_car, price)
            
        elif name == "Lamborgani":
            color_car = "Blue"
            model_car = "sports"
            price = "$40000"
            
            print(name, color_car, model_car, price)
            
        elif name == "Maruthi":
            color_car = "Gray"
            model_car = "Luxury"
            price = "$15000"
            
            print(name, color_car, model_car, price)
            
            
        else:
            print("There are no cars available as per your requirement")


# In[ ]:


car_list = ["Benz", "Ferrari", "BMW", "Lamborgani", "Honda"]


# In[ ]:


cars(car_list)


# ## Return Statement
# 
# Return statement is to return from a function or to breakout a function, optionally it returns a value from function
# A return statement with no arguments is the same as return None.

# In[ ]:


def calc_sum(x, y):

  return x, y


# In[ ]:


x_value, y_value = calc_sum(1, 2)


# In[ ]:


print(x_value, y_value)


# In[ ]:


def sum():
    x = 2
    y = 6
    z = x + y
    print(z)
    return z #none
                #output of that variable
    print(z)
    
    
    

sum()


# In[ ]:


def my_sum():
    x = 10
    print(x)
    return x
    print(12)
    
sum1 = my_sum()
print(sum1)


# In[ ]:


#return breaks the function
#It stores the output


# In[ ]:


def sum_num(arg1, arg2):
    total = arg1 + arg2
    print("printing total", total)
    return total

sum_num(10, 20)


# ## Scope of Variable
# All variables in a program may not be accessible at all locations in that program. 
# This depends on where you have declared a variable.
# 
# The scope of a variable determines the portion of the program where you can access a particular identifier. 
# There are two basic scopes of variables in Python −
# 
# Global variables
# 
# Local variables

# ## Global and Local Variables
# 
# Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.
# 
# These terms of global and local correspond to a variable's reach within a script or program. A global variable is one that can be accessed anywhere. A local variable is the opposite, it can only be accessed within its frame(function). The difference is that global variables can be accessed locally, but not modified locally inherently.
# 
# A local variable cannot be accessed globally, inherently.
# 

# In[ ]:


x = 6 #global variable
def example():
    print(x)
    z = 5
    print(z)
    
example()
    


# it just so happens that it is committed to memory before the function is called
# so we are able to iterate, or call it out, but we cannot do much else.

# In[ ]:


#Here, again, we are able to reference x, we are even able to print x+6... but we are not allowed to modify x
x_num = 6

def example2():
    # works
    print(x_num)
    x_num = x_num+5


# In[ ]:


example2()


# In[ ]:


#What if we'd like to modify x? Well, then we need to use global!
x_num = 6

def example3():
    global x_num
    print(x_num)
    x_num+=5
    print(x_num)


# In[ ]:


example3()


# How do we get around using them and referencing them locally?

# In[ ]:


x = 6

def example4():
    y_num = 10 #local
    print(y_num)
    
example4()


# In[ ]:


x = 6

def example4():
    y_num = 10
    y_num += 2
    print(y_num)
    
example4()


# In[ ]:


total = 0
def sum_num(arg1, arg2):
    # Add both the parameters and return them
    total = arg1 + arg2 #Here total is local variable
    print("print inside the function local total :", total )
    return total

sum_num(10, 20)
print("print outside the function global total :", total )
    


# <h2>lamda function</h2>
# 
# The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are throw-away functions, i.e. they are just needed where they have been created. Lambda functions are mainly used in combination with the functions map()

# In[ ]:


def sum(x=1):
    print(x+1)
    
    
sum()


# In[ ]:


f = lambda x: x+1
f(2)


# ## The Map function
# The advantage of the lambda operator can be seen when it is used in combination with the map() function. 
# map() is a function with two arguments:

# r = map(fun, seq)
# 
# #### The first argument func is the name of a function
# #### Second is sequence

# In[ ]:


def add(x, y): 
    return x + y
  
add(2, 3)


# In[ ]:


add = lambda x, y: x+y
print(add(2, 3))


# In[ ]:


def multiply2(x):
    return x * 2

#map(func, seq)
mult = map(multiply2, [1, 2, 3, 4, 5])
print(mult)
print(list(mult))


# In[ ]:


mult = map(lambda x: x*2, [1, 2, 3, 4, 5] )
print(list(mult))


# ### Iterating over a dictionary using map and lambda

# In[ ]:


#synatx
#map(function, sequence)
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

x_d1 = map(lambda x : x['name'], dict_a)

x_d2 = map(lambda x : x['points']*10,  dict_a) # Output: [100, 80]

x_d3 = map(lambda x : x['name'] == "python", dict_a) # Output: [True, False]

print(list(x_d1))
print(list(x_d2))
print(list(x_d3))


# ## Multiple iterables to the map function

# In[ ]:


list_a = [1, 2, 3]
list_b = [10, 20, 30]

x_d4 = map(lambda x, y: x + y, list_a, list_b)
print(list(x_d4))


# In[ ]:


#


# ## Python OOPS Tutorial

# Object is a Unique instance of Data Structure the defines by Its class. An object comprises both data members(Class Variables and Instance Variables)
# 
# Instance is a Individual object of certain class
# 
# Method a special kind of function that is defined in a class definition
# 
# The first argument of every class method, including init, is always a reference to the current instance of the class. By Convention, this argument is always named self

# In[ ]:


class car:
  carCount = 0
  def __init__(self, color, model):
    self.color = color
    self.model = model
    car.carCount +=1
    
  def displayCarCount(self):
    print("Total Count of cars are %d" % car.carCount)
    
  def showColorBrand(self):
    print("The Color and Brand of the Car is", self.color, self.model)


# carCount = Class Variable (This value shared across all functions). init = first method which calls class constructor. color, model are the instance variable. showColor, showBrand are the python functions.

# ## To Create Instance Object

# In[ ]:


#First Object
car1 = car("Red", "Ferrari")

#Second Object
car2 = car("Black", "Lamborgani")


# ## To Access Attributes

# In[ ]:


car1.showColorBrand()
car2.displayCarCount()


# ## Other Ways to Access Attributes

# The getattr(obj, name[, default]) − to access the attribute of object. The hasattr(obj,name) − to check if an attribute exists or not.
# 
# The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
# 
# The delattr(obj, name) − to delete an attribute.

# In[ ]:


getattr(car1, 'color')


# In[ ]:


hasattr(car1, 'model')


# In[ ]:


setattr(car1, 'color', 'BLACK')


# In[ ]:


delattr(car1, 'color')


# In[ ]:


hasattr(car1, 'color')


# In[ ]:




