import re
with open('AOC2018_3.data', 'r') as f:
    claims = f.read().split('\n')

class Claim:
    def __init__(self, id_num, x, y, width, heigth, squares):
        self.id = id_num
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.intact = True
        self.squares = squares
        


grid = []
for c in claims:
    id_num, x,y, width, heigth = re.search(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$',c).groups()
    id_num, x, y, w, h = int(id_num), int(x), int(y), int(width), int(heigth)
    squares = set()
    for i in range(x,x+w):
        for j in range(y,y+h):
            squares.add((i,j))
    grid.append(Claim(id_num, x,y, w,h, set(squares)))

commons = []
for i in range(len(grid)-1):
    for j in range(i+1, len(grid)):
        if grid[i].squares & grid[j].squares:
            grid[i].intact = False
            grid[j].intact = False
            commons.append(grid[i].squares & grid[j].squares)
print('part 1:', len(set.union(*commons)))
    
for g in grid:
    if g.intact:
        print('part 2:', g.id)
