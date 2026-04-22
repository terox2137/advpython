#SLIP - 1
#Q1. Write Python code to create a dictionary containing mobile names and their prices.Create DataFrame from this dictionary. Display the contents of DataFrame.#

import pandas as pd

# Creating dictionary
data = {
    "Mobile_Name": ["Samsung", "Redmi", "Realme", "iPhone"],
    "Price": [20000, 15000, 18000, 70000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Mobile DataFrame:")
print(df)

#Q.2-A
# cars module
def car_models():
    return ["Swift", "Baleno", "i20"]

# bikes module
def bike_models():
    return ["Pulsar", "Apache", "R15"]

# main program
print("Available Car Models:")
for car in car_models():
    print(car)

print("\nAvailable Bike Models:")
for bike in bike_models():
    print(bike)

## Q.2 - B
import os

files = os.listdir()

count = 0

for file in files:
    print(file)

    if file.endswith(".py"):
        count += 1

print("Total .py files:", count)

for file in files:
    if file.endswith(".py"):
        f = open(file, "r")
        print("\nContent of", file)
        print(f.read())
        f.close()
        break
-------------------------------------------------------------------------------------------------
## SLIP - 2
##Q1 – Vowels, Consonants, Special Symbols (10 MARKS)
s = input("Enter a string: ")

vowels = 0
consonants = 0
special = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Special Symbols:", special)

#Q2 – IPL DataFrame
import pandas as pd
import numpy as np

data = {
    "Player": ["Hardik Pandya","K L Rahul","Andre Russel","Jasprit Bumrah","Virat Kohli","Rohit Sharma"],
    "Team": ["Mumbai Indians","Kings Eleven","Kolkata Knight Riders","Mumbai Indians","RCB","Mumbai Indians"],
    "Category": ["Batsman","Batsman","Batsman","Bowler","Batsman","Batsman"],
    "BidPrice": [13,12,None,10,17,None],
    "Runs": [1000,2400,900,200,3600,3700]
}

df = pd.DataFrame(data)

print("DataFrame:\n",df)

# a) first 2 rows
print(df.head(2))

# b) last 3 rows
print(df.tail(3))

# c) check null values
print(df.isnull())

# d) replace null with mean
df["BidPrice"].fillna(df["BidPrice"].mean(), inplace=True)
print(df)

# e) most expensive player
print(df.loc[df["BidPrice"].idxmax()])

# f) players per team
print(df["Team"].value_counts())
-------------------------------------------------------------------------------------------------
#SLIP - 3
#Q.1
try:
    m = int(input("Enter value of m: "))
    n = int(input("Enter value of n: "))

    result = m / n
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

## Q.2
# factorial function
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

# power dictionary
power = {
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# accept number
n = int(input("Enter number: "))

# factorial
print("Factorial:", factorial(n))

# power
print("Power:", power.get(n, "Not available"))

# second vowel
print("Second vowel:", vowels[1])

-------------------------------------------------------------------------------------------------
##SLIP - 4
#Q.1
import random

# create list
lst = [10, 20, 30, 40, 50]

print("Original List:", lst)

# shuffle list
random.shuffle(lst)

print("Shuffled List:", lst)

#Q.2
import pandas as pd

data = {
    "Company": ["Apsara","Natraj","Cello","Parkar","Apsara"],
    "Count": [15,20,25,35,20],
    "Pencil": ["Pencil","Pen","Pen","Eraser","Pencil"],
    "Price": [250,200,600,900,300]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# a) rows with label Pencil
print("\nRows with Pencil:")
print(df[df["Pencil"]=="Pencil"])

# b) change Eraser count to 25
df.loc[df["Pencil"]=="Eraser","Count"] = 25
print("\nAfter updating Eraser count:")
print(df)

# c) only Company and Price columns
print("\nCompany and Price columns:")
print(df[["Company","Price"]])

# d) rows with Pencil and Pen
print("\nRows with Pencil and Pen:")
print(df[df["Pencil"].isin(["Pencil","Pen"])])

# e) rename Count to Quantity
df.rename(columns={"Count":"Quantity"}, inplace=True)
print("\nAfter renaming column:")
print(df)
-------------------------------------------------------------------------------------------------
##SLIP - 5
#Q.1
s = input("Enter a string: ")

words = s.split()

print("Words without vowels:")

for w in words:
    if not any(v in w.lower() for v in "aeiou"):
        print(w)

##Q.2
# account module
def open_account(name):
    print("Account created successfully for", name)

# loan module
def apply_loan(amount):
    print("Loan applied successfully for amount:", amount)

# main program
name = input("Enter account holder name: ")
amount = int(input("Enter loan amount: "))

open_account(name)
apply_loan(amount)

-------------------------------------------------------------------------------------------------
# SLIP - 6
# Q.1
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    if not a.isnumeric() or not b.isnumeric():
        raise TypeError("Input must be numeric")

    a = int(a)
    b = int(b)

    print("Sum:", a + b)

except TypeError as e:
    print(e)

## Q.2
import pandas as pd

data = {
    "Label": ["Pencil","Pencil","Pen","Pen","Eraser"],
    "Company": ["Apsara","Natraj","Cello","Parkar","Apsara"],
    "Count": [15,20,25,35,20],
    "Price": [250,200,600,900,300]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# a) rows with Pencil
print("\nRows with Pencil:")
print(df[df["Label"]=="Pencil"])

# b) change Eraser count to 25
df.loc[df["Label"]=="Eraser","Count"] = 25

# c) only Company and Price
print("\nCompany and Price:")
print(df[["Company","Price"]])

# d) rows with Pencil and Pen
print("\nRows with Pencil and Pen:")
print(df[df["Label"].isin(["Pencil","Pen"])])

# e) delete Count column
df = df.drop("Count", axis=1)

print("\nAfter deleting Count column:")
print(df)

-------------------------------------------------------------------------------------------------
#SLIP - 7
#Q.1
import re

s = input("Enter a string: ")

# remove special characters
clean = re.sub(r'[^A-Za-z\s]', '', s)

# extract words starting with capital letter
words = clean.split()

print("Words starting with capital letter:")
for w in words:
    if w[0].isupper():
        print(w)

print("Modified String:", clean)

#Q.2 - B
filename = input("Enter file name: ")

try:
    f = open(filename, "r")
    content = f.read()
    f.close()

    # copy to new file
    newfile = "copy.txt"
    f2 = open(newfile, "w")
    f2.write(content)
    f2.close()

    # display new file
    f3 = open(newfile, "r")
    text = f3.read()
    print("Content of new file:\n", text)

    print("Characters:", len(text))
    print("Words:", len(text.split()))
    print("Lines:", len(text.split("\n")))

    f3.close()

except FileNotFoundError:
    print("File does not exist")
-------------------------------------------------------------------------------------------------
## SLIP -8
## Q.1
def area(radius):
    return 3.14 * radius * radius

r = float(input("Enter radius: "))

result = area(r)

print("Area of Circle:", result)

## Q.2
import random

# list
lst = [10,20,30,40,50]

# string
s = "PYTHON"

# tuple
t = (1,2,3,4,5)

print("Random elements from list:", random.sample(lst,3))

print("Random elements from string:", random.sample(s,3))

print("Random elements from tuple:", random.sample(t,3))
-------------------------------------------------------------------------------------------------
## SLIP 9
## Q.1
def even_generator(n):
    for i in range(2, n+1, 2):
        yield i

n = int(input("Enter value of n: "))

print("Even numbers up to", n)

for num in even_generator(n):
    print(num)

## Q.2
import pandas as pd

# Student 1 DataFrame
student1 = pd.DataFrame({
    "ID": ["S1","S2","S3","S4","S5"],
    "Name": ["Anita","Sakshi","Om","Raj","Kanika"],
    "Age": [18,23,20,21,20]
})

# Student 2 DataFrame
student2 = pd.DataFrame({
    "ID": ["S2","S4","S5","S6","S7"],
    "City": ["Pune","Nashik","Mumbai","Delhi","Nanded"],
    "Marks": [97,78,86,66,54]
})

print("Student 1 DataFrame")
print(student1)

print("\nStudent 2 DataFrame")
print(student2)

# join dataframes
student3 = pd.merge(student1, student2, on="ID")

print("\nJoined DataFrame")
print(student3)

-------------------------------------------------------------------------------------------------
## SLIP - 12
## Q.1
## MAKE CSV FILE FIRST
##EX.
Name,Designation,Salary
Rahul,Manager,50000
Amit,Developer,40000
Neha,Analyst,45000
Riya,HR,35000

##Q.1
import pandas as pd

df = pd.read_csv("data.csv")

print("DataFrame:")
print(df)

print("\nStatistical Information:")
print(df.describe())

## Q.2
import time
from datetime import datetime

# current local time
print("Local Time:", time.ctime())

# UTC time
print("UTC Time:", time.gmtime())

# accept date-time
dt = input("Enter date-time (DD-MM-YYYY HH:MM:SS): ")

# parse string
parsed = datetime.strptime(dt, "%d-%m-%Y %H:%M:%S")

# format in two ways
print("Format 1:", parsed.strftime("%d/%m/%Y %H:%M"))
print("Format 2:", parsed.strftime("%A, %B %d %Y"))
-------------------------------------------------------------------------------------------------
##SLIP - 13
## Q.1

import time

# current time in seconds
current = time.time()

print("Current time in seconds:", current)

# convert seconds to readable string
print("Readable time:", time.ctime(current))

# convert seconds to struct_time in UTC
print("UTC struct_time:", time.gmtime(current))

## Q.2 - B
import pandas as pd

# Student 1
student1 = pd.DataFrame({
    "ID": ["S1","S2","S3","S4","S5"],
    "Name": ["Anita","Sakshi","Om","Raj","Kanika"],
    "Age": [18,23,20,21,20]
})

# Student 2
student2 = pd.DataFrame({
    "ID": ["S2","S4","S5","S6","S7"],
    "City": ["Pune","Nashik","Mumbai","Delhi","Nanded"],
    "Marks": [97,78,86,66,54]
})

print("Student 1")
print(student1)

print("\nStudent 2")
print(student2)

# join dataframes
student3 = pd.merge(student1, student2, on="ID")

print("\nJoined DataFrame")
print(student3)
-------------------------------------------------------------------------------------------------
##SLIP - 14
##Q.1
import re

s = input("Enter string: ")
sub = input("Enter substring: ")

pattern = "^" + sub   # check at beginning

if re.match(pattern, s):
    print("Substring is present at the beginning.")
else:
    print("Substring is NOT present at the beginning.")

##Q.2 - B
# factorial function
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

# power dictionary
power = {2:4, 3:9, 4:16, 5:25}

# vowels list
vowels = ['a','e','i','o','u']

n = int(input("Enter number: "))

print("Factorial:", factorial(n))
print("Power:", power.get(n, "Not available"))
print("Second vowel:", vowels[1])
-------------------------------------------------------------------------------------------------
## SLIP - 15

## Q.1
import time

# current time in seconds
t = time.time()

# a) convert seconds to struct_time in UTC
utc_time = time.gmtime(t)
print("UTC struct_time:", utc_time)

# b) convert struct_time to formatted string
formatted = time.strftime("%d-%m-%Y %H:%M:%S", utc_time)
print("Formatted Time:", formatted)

##Q.2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def library():
    return """
    <h1 style='text-align:center;'>City Library</h1>

    <table border="1">
        <tr>
            <th>Title</th>
            <th>Author</th>
        </tr>
        <tr>
            <td>Python Programming</td>
            <td>Guido van Rossum</td>
        </tr>
        <tr>
            <td>Data Science</td>
            <td>Joel Grus</td>
        </tr>
        <tr>
            <td>Artificial Intelligence</td>
            <td>Andrew Ng</td>
        </tr>
    </table>

    <p style="color:blue; font-weight:bold;">
    Reading is to the mind what exercise is to the body.
    </p>
    """

app.run()
-------------------------------------------------------------------------------------------------
## SLIP 16
## Q.1

import re

word = input("Enter word: ")

pattern = r"^[bh]i?t$|^[bh]u?t$|^[bh]a?t$"

if re.match(pattern, word):
    print("Valid three letter word")
else:
    print("Invalid word")
    
##Q.2 - B
def car_models():
    return ["Swift","Baleno","i20"]

def bike_models():
    return ["Pulsar","Apache","R15"]

print("Available Car Models:")
for c in car_models():
    print(c)

print("\nAvailable Bike Models:")
for b in bike_models():
    print(b)

-------------------------------------------------------------------------------------------------
## SLIP 17
## Q.1

s = input("Enter string: ")

# replace space with colon
s = s.replace(" ", ":")

# replace comma with dot
s = s.replace(",", ".")

print("Modified string:", s)

## Q.2
import random

# list
lst = [10,20,30,40,50]

# string
s = "PYTHON"

# tuple
t = (1,2,3,4,5)

print("Random elements from list:", random.sample(lst,3))
print("Random elements from string:", random.sample(s,3))
print("Random elements from tuple:", random.sample(t,3))

-------------------------------------------------------------------------------------------------
## SLIP 19
## Q.1
import random

# deck of cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

deck = []

for s in suits:
    for r in ranks:
        deck.append(r + " of " + s)

# shuffle deck
random.shuffle(deck)

print("Cards obtained by user in 5 attempts:")

for i in range(5):
    print(deck[i])

##Q.2
import os

path = os.getcwd()

print("Current Directory:", path)

items = os.listdir(path)

for item in items:
    if os.path.isfile(item):
        print(item, "- File")
    else:
        print(item, "- Folder")

-------------------------------------------------------------------------------------------------
## SLIP 20
## Q.1
s = input("Enter string: ")

v = c = sp = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v += 1
        else:
            c += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Special Symbols:", sp)

##Q.2
filename = input("Enter file name: ")
pos = int(input("Enter byte position: "))

try:
    f = open(filename,"r")

    f.seek(pos)

    print("Content from given position:")
    print(f.read())

    f.close()

except FileNotFoundError:
    print("File does not exist")

-------------------------------------------------------------------------------------------------
## SLIP 21
## Q.1
import pandas as pd

data = {
"Subject_Name":["Math","Physics","Chemistry","Biology","English","Computer"],
"Marks":[85,78,82,75,80,90]
}

df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

##Q.2
filename = input("Enter file name: ")

try:
    f = open(filename,"r")

    text = f.read()

    print("File Content:")
    print(text)

    print("Characters:", len(text))
    print("Words:", len(text.split()))
    print("Lines:", len(text.split("\n")))

    f.close()

except FileNotFoundError:
    print("File does not exist")

-------------------------------------------------------------------------------------------------
## SLIP 22
## Q.1
try:
    m = int(input("Enter value of m: "))
    n = int(input("Enter value of n: "))

    result = m / n
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

##Q.2
import pandas as pd

# Student 1
student1 = pd.DataFrame({
    "ID":["S1","S2","S3","S4","S5"],
    "Name":["Anita","Sakshi","Om","Raj","Kanika"],
    "Age":[18,23,20,21,20]
})

# Student 2
student2 = pd.DataFrame({
    "ID":["S2","S4","S5","S6","S7"],
    "City":["Pune","Nashik","Mumbai","Delhi","Nanded"],
    "Marks":[97,78,86,66,54]
})

print("Student 1:")
print(student1)

print("\nStudent 2:")
print(student2)

# merge
student3 = pd.merge(student1, student2, on="ID")

print("\nMerged DataFrame:")
print(student3)

-------------------------------------------------------------------------------------------------
## SLIP 25
## Q.1
import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

deck = []

for s in suits:
    for r in ranks:
        deck.append(r + " of " + s)

random.shuffle(deck)

print("Cards obtained in 5 attempts:")

for i in range(5):
    print(deck[i])

##Q.2
def cal_interest(amount, year):
    rate = 0.05
    return amount * rate * year

def convert(amount):
    usd = amount * 0.012
    return usd


amt = float(input("Enter amount: "))
yr = int(input("Enter years: "))

print("Simple Interest:", cal_interest(amt, yr))

print("Amount in USD:", convert(amt))

-------------------------------------------------------------------------------------------------
## SLIP 26
## Q.1
s = input("Enter string: ")

# remove whitespaces
s = s.replace(" ", "")

print("Modified string:", s)

##Q.2
def car_models():
    return ["Swift","Baleno","i20"]

def bike_models():
    return ["Pulsar","Apache","R15"]

print("Available Car Models:")
for c in car_models():
    print(c)

print("\nAvailable Bike Models:")
for b in bike_models():
    print(b)

-------------------------------------------------------------------------------------------------
## SLIP 27
## Q.1
import random
import math

# generate random radius
r = random.randint(1,10)

# circumference formula
circumference = 2 * 3.14 * r

print("Radius:", r)
print("Circumference:", circumference)

##Q.2
import re

password = input("Enter password: ")

pattern = r"^(?=.*[a-z])(?=.*[0-9])(?=.*[$#@]).{6,12}$"

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")

-------------------------------------------------------------------------------------------------
## SLIP 29
## Q.1

import pandas as pd

# read csv file
df = pd.read_csv("Iris.csv")

print("DataFrame Contents:")
print(df)

print("\nStatistical Information:")
print(df.describe())

##Q.2
filename = input("Enter file name: ")
text = input("Enter string to append: ")

try:
    f = open(filename, "a")
    f.write("\n" + text)
    f.close()

    f = open(filename, "r")
    print("File Content:")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File does not exist")

-------------------------------------------------------------------------------------------------
## SLIP 30
## Q.1
s = input("Enter string: ")

# replace a with *
s = s.replace("a","*")

print("Modified string:", s)

##Q.2
def check_pass_fail(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


n = int(input("Enter number of students: "))

pass_count = 0
fail_count = 0

for i in range(n):
    m = int(input("Enter marks: "))
    result = check_pass_fail(m)

    print("Result:", result)

    if result == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("Total Passed:", pass_count)
print("Total Failed:", fail_count)

-------------------------------------------------------------------------------------------------
