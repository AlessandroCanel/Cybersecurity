# Define a random password generator. The password should contain 10 characters. Type of characters: alphanumeric
def psw():
    import random
    p = int(input("password size "))
    x = ''
    string = ''

    # this cycle allows me to define the length of the password, for a more usable program
    while p:
        x = x + '0'
        p -= 1

    for z in x:
        string = string + chr(random.randint(48, 90))

    print(string)
