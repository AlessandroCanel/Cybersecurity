import re


def cap():
    def binary(one):
        two = one.replace("ONE", "1")
        two = two.replace("ZERO", "0")
        return two

    with open('CapitaliInput.txt', 'r') as file:
        phrase = file.read().replace('\n', '')

    result = re.sub('[^A-Z]', '', phrase)

    x = input("Would you like to binary? y/n  ")

    if x == 'y':
        AlternativeOutput = binary(result)
        print(AlternativeOutput, file=open("output.txt", "a"))
    else:
        print(result, file=open("output.txt", "a"))
