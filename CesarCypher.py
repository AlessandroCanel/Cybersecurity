def ces():
    with open('InputCesarCypher.txt', 'r') as file:
        phase = file.read().replace('\n', '')

    result = ''

    y = int(input("say how much you want to shift "))

    for x in phase:
        if x != " ":
            # deve essere tra 65 e 90
            if (ord(x) + y) > 90:
                result = result + chr(ord(x) + y - 26)
            elif (ord(x) + y) < 65:
                result = result + chr(ord(x) + y + 26)
            else:
                result = result + chr(ord(x) + y)
        else:
            result = result + ' '
    # This program moves the words ou or down the alphabet
    print(result, file=open("output.txt", "a"))
