import sys

type = sys.argv[1]

if type == "t2.micro":
    print("instance charges 2 dollars")
elif type == "t2.medium":
    print("instance charges 4 dollars")
elif type == "t2.large":
    print("instance charges 8 dollars")
else :
    print("provide valid type")