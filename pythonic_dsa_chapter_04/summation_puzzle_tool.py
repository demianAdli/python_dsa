"""This program helps when we want to use all the letters
for the game"""

letters = "abcdefghijklmnopqrstuvwxyz"
print(len(letters))
alphabet_index = {letter: letters.index(letter) for letter in letters}
print(alphabet_index)

seven = [x + y for x in alphabet_index for y in alphabet_index
         if alphabet_index[x] + alphabet_index[y] == 7]
print(seven)


