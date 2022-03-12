import sys

dict = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--.."
}

morseCode = []

for word in input("Enter string \n").lower().split(" "):
    morseWord = []
    for letter in word:
        morseWord.append(dict[letter])
    
    morseCode.append(" ".join(morseWord))

for word in morseCode:
    print(word)
