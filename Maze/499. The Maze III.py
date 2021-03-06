"""
Maze I: ask True or False
Maze II: ask min steps
Maze III: ask the path with min steps (backtrack)

The code below can solve all Maze I, II, III
Use minHeap to track of:
  "nx, ny" turning point (required for all Maze I, II, III)
  "nd" number of steps (new to MazeII, also can be used to speed up Maze I by 3x)
  "path" string records path (new to Maze III)
"""

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        Q = [[0]+ball+['']]
        m = len(maze)
        n = len(maze[0])
        dirs = {(-1,0):'u',(1,0):'d',(0,-1):'l', (0,1):'r'} #m/i direction is up-down, n/j direction is left-right.
        
        paths =[]
        while Q:
            d, x, y, path = heapq.heappop(Q)
            maze[x][y]='v'
            for (i, j), direction in dirs.items():
                nd, nx, ny = d, x, y
                while 0<=nx+i<m and 0<=ny+j<n and maze[nx+i][ny+j]!=1:
                    nd, nx, ny = nd+1, nx+i, ny+j
                    if hole[0]==nx and hole[1]==ny:
                        paths.append( [nd, path+direction])
                        break
                if maze[nx][ny]==0:
                    heapq.heappush(Q, (nd, nx, ny, path+direction))
                    
        return heapq.nsmallest(1, paths)[0][1] if paths else 'impossible'

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        Q = [[0]+ball+['']]
        m = len(maze)
        n = len(maze[0])
        dirs = {(-1,0):'u',(1,0):'d',(0,-1):'l', (0,1):'r'} #m/i direction is up-down, n/j direction is left-right.
        
        paths =[]
        while Q:
            d, x, y, path = heapq.heappop(Q)
            maze[x][y]='v'
            for (i, j), direction in dirs.items():
                nd, nx, ny = d, x, y
                while 0<=nx+i<m and 0<=ny+j<n and maze[nx+i][ny+j]!=1:
                    nd, nx, ny = nd+1, nx+i, ny+j
                    if hole[0]==nx and hole[1]==ny:
                        if paths and nd <= paths[0][0] or not paths:  
                            heapq.heappush(paths, [nd, path+direction])
                        break
                if maze[nx][ny]==0:
                    heapq.heappush(Q, (nd, nx, ny, path+direction))
                    
        return paths[0][1] if paths else 'impossible'
