# Let's begin with exercise 1, turn an abc string into +2 ASCII
def cde():
    a = "abc"
    string: str = ""

    for x in a:
        string = string + chr(ord(x) + 2)

    print(string)

# chr simply translates from int to chr, ord() returns the corresponding ASCII value of character
# and after adding integer to it, chr() again converts it into character.

# the output is "cde"
