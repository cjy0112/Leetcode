class Solution(object):
    def isPathCrossing(self, path):
        xy = [(0,0)]
        for dir in path:
            past = xy[-1]
            if dir == 'N':
                present = (past[0],past[1]+1)
            elif dir == 'S':
                present = (past[0],past[1]-1)
            elif dir == 'E':
                present = (past[0]+1,past[1])
            elif dir == 'W':
                present = (past[0]-1,past[1])
            if present in xy:
                return True
            xy.append(present)
        return False
      
