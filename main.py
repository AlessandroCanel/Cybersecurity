import re


def binary(one, two):
    for y in one:
        if y == 'Z':
            two = two + '0'
        elif y == 'O':
            two = two + '1'
    return two


with open('challenge.txt', 'r') as file:
    phrase = file.read().replace('\n', '')

result = re.sub('[^A-Z]', '', phrase)

x = input("Would you like to binary? y/n  ")

if x == 'y':
    AlternativeOutput = ''
    AlternativeOutput = binary(result, AlternativeOutput)
    print(AlternativeOutput, file=open("output.txt", "a"))
else:
    print(result, file=open("output.txt", "a"))
