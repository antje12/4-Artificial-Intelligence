import sys

freq = {}

for word in input("Enter string \n").split(" "):
    if word in freq:
        freq[word] = freq[word] + 1

    else:
        freq[word] = 1

print(freq)
