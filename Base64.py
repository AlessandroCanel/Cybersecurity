# Let's see how this base 64 stuff works

import base64


def based():
    with open('InputBase64.txt', 'r') as file:
        phase = file.read()

    c = input("decode or encode? ")
    times = int(input("How many times? "))

    while times != 0:
        if c == "encode":
            phase = base64.b64encode(bytes(phase, "utf-8"))
            phase = phase.decode("utf-8")
            times -= 1
        elif c == "decode":
            phase = base64.b64decode(phase)
            times -= 1
        else:
            print("Wrong input")
            times -= times

    # basically this hot trash of a code simply transforms into binary and then into ascii
    if c == "decode":
        phase = phase.decode("utf-8")
    print(phase, file=open("output.txt", "a"))
