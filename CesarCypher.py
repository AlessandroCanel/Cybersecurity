with open('Lesson4es3.txt', 'r') as file:
    phase = file.read().replace('\n', '')

result = ''

y = int(input("say how much you want to shift "))

for x in phase:
    result = result + chr(ord(x) + y)
# Programma muove i caratteri
print(result, file=open("output.txt", "a"))
