def ces():
    with open('InputCesarCypher.txt', 'r') as file:
        phase = file.read().replace('\n', '')

    result = ''

    y = int(input("say how much you want to shift "))

    for x in phase:
        if x != " ":
            result = result + chr(ord(x) + y)
    # This program moves the words ou or down the alphabet
    print(result, file=open("output.txt", "a"))
