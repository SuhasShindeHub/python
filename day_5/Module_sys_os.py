import sys
import os # For environment variables - to store sensitive information

def add(a, b):
    add = a + b
    return add

def sub(a, b):
    sub = a - b
    return sub

def multi(a, b):
    multi = a * b
    return multi

def div(a, b):
    div = a / b
    return div

a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

if operation == "add":
    output = add(a, b)
    print(output)


# use command export password="abc"
password = os.getenv("dummypass")
print(password)