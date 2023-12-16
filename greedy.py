from Maze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))

def greedy(m, start=None):
    if start is None:
        start = (m.rows, m.cols)

    open = PriorityQueue()
    open.put((h(start, m._goal), start))
    aPath = {}
    searchPath = [start]

    while not open.empty():
        _, currCell = open.get()

        if currCell == m._goal:
            break

        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                if childCell not in aPath:
                    open.put((h(childCell, m._goal), childCell))
                    aPath[childCell] = currCell

        searchPath.append(currCell)

    fwdPath = {}
    cell = m._goal

    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return searchPath, aPath, fwdPath

if __name__ == '__main__':
    m = maze(10, 10)
    m.CreateMaze()
    searchPath, aPath, fwdPath = greedy(m)

    a = agent(m, footprints=True, color=COLOR.blue, filled=True, shape='arrow')
    b = agent(m, 1, 1, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))
    c = agent(m, footprints=True, color=COLOR.red)

    m.tracePath({a: searchPath}, delay=50)
    m.tracePath({b: aPath}, delay=50)
    m.tracePath({c: fwdPath}, delay=50)

    l = textLabel(m, 'Greedy Path Length', len(fwdPath) + 1)
    l = textLabel(m, 'Greedy Search Length', len(searchPath))
    
    m.run()