class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        
        x=0
        y=0
        a=set()
        a.add((x,y))
        for i in path:
            if i =='N':
                y+=1
                if (x,y) in a:
                    return True
                else:
                    a.add((x,y))       
            elif i=='S':
                y-=1
                if (x,y) in a:
                    return True
                else:
                    a.add((x,y))
            elif i=='E':
                x+=1
                if (x,y) in a:
                    return True
                else:
                    a.add((x,y))
            elif i=='W':
                x-=1
                if (x,y) in a:
                    return True
                else:
                    a.add((x,y))
            print(a)
        return False
