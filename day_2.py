from collections import Counter

with open('day_2.data') as f:
    data = f.read().split()

# checksum, product of the number of id number with exactly 3 identical letter and number of id with exactly 2 identical letter
threes = 0
twos = 0
for box in data:
    if 3 in Counter(box).values():
        threes += 1
    if 2 in Counter(box).values():
        twos += 1
print('Part 1:',twos * threes)

def close(id1, id2):
    # true if id1 and id2 differ by one and only one character
    return sum(len(set(p)) for p in zip(id1,id2)) == (len(id1) + 1)

# print common characters of id1 and id2
for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        if close(data[i],data[j]):
            print('Part 2:', ''.join(p[0] for p in zip(data[i],data[j]) if len(set(p))==1))
