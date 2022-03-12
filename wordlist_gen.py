import itertools


s = input("string to be permuted: ")
#size = int(input("Inform the length for the word to be generated in a row: "))

output = itertools.permutations(s, len(s))

for i in output:
    print(''.join(i))
