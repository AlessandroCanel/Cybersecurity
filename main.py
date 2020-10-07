import re

with open('challenge.txt', 'r') as file:
    phrase = file.read().replace('\n', '')

result = re.sub('[^A-Z]', '', phrase)

print(result, file = open("output.txt", "a"))
