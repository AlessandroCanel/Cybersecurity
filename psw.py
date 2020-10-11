# Define a random password generator. The password should contain 10 characters. Type of characters: alphanumeric
def psw():
    import random
    x = '0000000000'
    string = ''

    for z in x:
        string = string + chr(random.randint(48, 90))

    print(string)