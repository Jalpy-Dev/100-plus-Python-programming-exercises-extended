# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

usr_input = input('Enter a sentence por favor: ').split(' ')
wrd_frequency = {}
for word in usr_input:
    wrd_frequency.setdefault(word, usr_input.count(word))

words = sorted(list(wrd_frequency.keys()))

for key in words:
    print(f'{key}: {wrd_frequency.get(key)}')
