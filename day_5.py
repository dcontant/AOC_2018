'''
remove all lowercase-uppercase pairs, return the final length of the strings ( test data is length 16, actual data = 50000
dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
'''


with open('AOC2018_5.data', 'r') as f:
    data = f.read()

def same_pol(i):
    '''checks if two adjacent are a uppper-lower pair, tally the total number found, '''
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


'''
for all letters, remove all instances of uppercase-lowercase  (regardless of polarity), 
fully react the remaining polymer, and measure its length.
find the shortest length obtained
'''
# Part 2
from string import ascii_lowercase as units

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
