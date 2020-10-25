# This is the main, it will be used to access all of the other python scripts if i see fit
# I am aware this is not best practice but whatever

import Capitali
import CesarCypher
import letters
import calc
import psw
import Base64

file = open("output.txt", "r+")
file.truncate(0)
file.close()

print("Select witch program ")
print("1) Cesar")
print("2) Capital")
print("3) ABC")
print("4) Calc")
print("5) Psw")
print("6) Base64")
print("write 'help' for details")

i = input()

if i == '1':
    CesarCypher.ces()
elif i == '2':
    Capitali.cap()
elif i == '3':
    letters.cde()
elif i == '4':
    calc.calc()
elif i == '5':
    psw.psw()
elif i == '6':
    Base64.based()
elif i == 'help':
    print("1) Cesar adds or decreases the spot in an ASCII alphabet for the whole string")
    print("2) Capital takes all the Capital words and gives you the option to turn 'ZERO' into 0 and 'ONE' into 1")
    print("3) Just shifts ascii value from abc string to cde")
    print("4) Calculator")
    print("5) Creates random password from string")
    print("6) Takes the txt InputBase64 and just decodes for n times")
else:
    print("Incorrect input")
