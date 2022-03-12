import sys

freq = {}

for word in input("Enter string \n").split(" "):
    freq[word] = 1 + freq.get(word, 0)

print(freq)
