from string import ascii_lowercase as units

with open('AOC2018_5.data', 'r') as f:
    data = f.read()

def same_pol(i):
    global n
    global reacts
    j = i+1
    while abs(ord(data[i])-ord(data[j])) == 32:
        n += 2
        reacts |= set([i,j])
        while i in reacts: # find the lower bound of a contiguous reactions substring
            i -= 1
        j += 1
        if i<0 or j>len(data)-1:
            break
    return j
            
# Part 1 
n = 0
reacts = set()
i = 0
while i<len(data)-1:
    i = same_pol(i)            
print('part 1:', len(data)-n)


# Part 2
temp = data[:]
final_length = []
for u in units:
    data = data.replace(u, '')
    data = data.replace(u.upper(), '')
    n = 0
    i = 0
    reacts = set()
    while i<len(data)-1:
        i = same_pol(i)            
    final_length.append(len(data)-n)
    data = temp
print('Part 2:', min(final_length))
