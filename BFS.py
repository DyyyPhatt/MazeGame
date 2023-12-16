from Maze import maze,agent,textLabel,COLOR
from collections import deque

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
    # print(f'{bfsPath}')
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath

if __name__=='__main__':
    m=maze(10,10)
    m.CreateMaze()
    bSearch,bfsPath,fwdPath=BFS(m)
    a=agent(m,footprints=True,shape='arrow',filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,shape='square',filled=True,goal=(m.rows,m.cols))
    c=agent(m,footprints=True,color=COLOR.red,shape='square',filled=False)

    m.tracePath({a:bSearch},delay=50)
    m.tracePath({b:bfsPath},delay=50)
    m.tracePath({c:fwdPath},delay=50)

    l=textLabel(m,'BFS Path Length',len(fwdPath)+1)
    l=textLabel(m,'BFS Search Length',len(bSearch))

    m.run()