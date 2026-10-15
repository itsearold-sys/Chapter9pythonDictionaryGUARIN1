
mbox = input('Enter file name: ')
fname = open("mbox-short.txt")
counts = dict

for line in fname:
    line = line.strip()

if line.startswith('@ '):
    word = line.split()
    for word in fname:
        counts[word] = counts.get(word, 0) + 1
print("Counts", counts)




