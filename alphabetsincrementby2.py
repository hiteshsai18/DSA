#take n=hitesh and add +2 to each alphabet's number to get output as jkvguj without using ascii.

alphabets = 'abcdefghijklmnopqrstuvwxyz'
n = 'hitesh'
output = ''
index_map = {char: i for i, char in enumerate(alphabets)}
for char in n:
    index = index_map[char]
    new_index = (index + 2) % 26
    output += alphabets[new_index]
print(output)



