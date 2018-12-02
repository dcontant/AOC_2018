from itertools import cycle

with open('day_1.data') as f:
    data = f.read().split()
    
print('part 1: ',sum(int(d) for d in data))

data = cycle(data)
visited = set([0])
f = 0
i = 0
while True:
    f += int(next(data))
    if f in visited:
        print('part 2: ',f)
        break
    visited.add(f)
