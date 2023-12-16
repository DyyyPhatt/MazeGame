from Maze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

def UCS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)

    open = PriorityQueue()
    open.put((0, start))
    ucsPath = {}
    cost = {row: float("inf") for row in m.grid}
    cost[start] = 0

    searchPath = [start]

    while not open.empty():
        currCost, currCell = open.get()
        searchPath.append(currCell)

        if currCell == m._goal:
            break

        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                temp_cost = cost[currCell] + 1

                if temp_cost < cost[childCell]:
                    ucsPath[childCell] = currCell
                    cost[childCell] = temp_cost
                    open.put((temp_cost, childCell))

    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[ucsPath[cell]] = cell
        cell = ucsPath[cell]

    return searchPath, ucsPath, fwdPath

if __name__ == '__main__':
    m = maze(10, 10)
    m.CreateMaze()

    searchPath, ucsPath, fwdPath = UCS(m)
    a = agent(m, footprints=True, color=COLOR.blue, filled=True, shape='arrow')
    b = agent(m, 1, 1, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))
    c = agent(m, footprints=True, color=COLOR.red)

    m.tracePath({a: searchPath}, delay=10)
    m.tracePath({b: ucsPath}, delay=50)
    m.tracePath({c: fwdPath}, delay=50)

    l = textLabel(m, 'UCS Path Length', len(fwdPath) + 1)
    l = textLabel(m, 'UCS Search Length', len(searchPath))
    
    m.run()