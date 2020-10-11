# now we continue with exercise 2
# Define a calculator with three variables
# First integer, second integer, type of operation (0 addition)

def calc():
    a = int(input("First number: "))
    b = int(input("Second number: "))
    c = int(input("0 add, 1 sub, 2 div, 3 multiply "))

    if c == 0:
        print(a + b)
    elif c == 1:
        print(a - b)
    elif c == 2:
        print(a / b)
    elif c == 3:
        print(a * b)
    else:
        print("Third value not correct")

# elif works like in else if with c++, for defining an int in input you need to do like so
