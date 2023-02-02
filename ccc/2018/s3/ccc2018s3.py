WALL = 0
CAMERA = 1

class Node:
    def __init__(self):
        self.watched = False
        self.distance = -1
    def __repr__(self):
        return "."

class Conveyor:
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"
    def __init__(self, direction):
        self.direction = direction
        self.connections = []
    def __repr__(self):
        return self.direction


r, c = (int(x) for x in input().split())

nodes = []
start = None
rows = []
cameras = []
for i in range(r):
    raw_row = input()
    row = []
    for j, letter in enumerate(raw_row):
        if letter == "W":
            row.append(WALL)
        elif letter == "C":
            cameras.append((i, j))
            row.append(CAMERA)
        elif letter == ".":
            node = Node()
            nodes.append(node)
            row.append(node)
        elif letter == "S":
            start = j, i
            node = Node()
            node.distance = 0
            row.append(node)
        else:
            row.append(Conveyor(letter))
    rows.append(row)

for y, x in cameras:
    up = 1
    while y - up >= 0:
        item = rows[y - up][x]
        if isinstance(item, Node):
            item.watched = True
        if item == WALL:
            break
        up += 1

    down = 1
    while y + down < r:
        item = rows[y + down][x]
        if isinstance(item, Node):
            item.watched = True
        if item == WALL:
            break
        down += 1

    left = 1
    while x - left >= 0:
        item = rows[y][x - left]
        if isinstance(item, Node):
            item.watched = True
        if item == WALL:
            break
        left += 1

    right = 1
    while x + right < c:
        item = rows[y][x + right]
        if isinstance(item, Node):
            item.watched = True
        if item == WALL:
            break
        right += 1

unvisited = [] if rows[start[1]][start[0]].watched else [start]

while unvisited:
    x, y = unvisited.pop()
    current = rows[y][x]
    for ox, oy in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if ox in range(c) and oy in range(r):
            neighbor = rows[oy][ox]
            if isinstance(neighbor, Conveyor):
                conveyors = [(ox, oy)]
                good = True
                while True:
                    if neighbor.direction == Conveyor.UP:
                        oy -= 1
                    elif neighbor.direction == Conveyor.DOWN:
                        oy += 1
                    elif neighbor.direction == Conveyor.LEFT:
                        ox -=1
                    elif neighbor.direction == Conveyor.RIGHT:
                        ox += 1
                    if (ox, oy) in conveyors:
                        good = False
                        break
                    target = rows[oy][ox]
                    if isinstance(target, Conveyor):
                        neighbor = target
                    elif isinstance(rows[oy][ox], Node):
                        neighbor = target
                        break
                    else:
                        break
                if not good:
                    continue
            if isinstance(neighbor, Node):
                if neighbor.watched == True:
                    continue
                elif neighbor.distance == -1:
                    neighbor.distance = current.distance + 1
                    unvisited.append((ox, oy))
                elif neighbor.distance > current.distance + 1:
                    neighbor.distance = current.distance + 1
                    unvisited.append((ox, oy))

for node in nodes:
    print(node.distance)