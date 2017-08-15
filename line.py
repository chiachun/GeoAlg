import numpy as np


class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class seg:
    def __init__(self, p1, p2):
        self.horizontal = False
        
        if p2.y > p1.y:
            self.u = p2
            self.d = p1
        else:
            self.u = p1
            self.d = p2
    
        if p2.y == p1.y:
            self.horizontal = True
        
        self.a = (p2.y - p1.y) / (p2.x- p1.x) # slope
        self.b = p1.y - self.a * p1.x # y-intercept
    def intersect(self, seg):
        x = (seg.b - self.b) / (self.a - seg.a)
        y = self.a * x + self.b
        return (x,y)
    
def dot(a,b):
    return a.x*b.x + a.y*b.y


def cross(a,b):
    return a.x*b.y - a.y*b.x

p1 = point(1,2)
p2 = point(3,4)
p3 = point(0,0)
p4 = point(1,2)
np1 = np.array([1,2])
np2 = np.array([3,4])

print "dot", np.dot(np1,np2) == dot(p1,p2)
print "cross", np.cross(np1,np2) == cross(p1,p2)

seg1 = seg(p1,p2)
seg2 = seg(p3,p4)

print seg1.a, seg1.b
print seg2.a, seg2.b

intersection = seg1.intersect(seg2)
print "intersection: ", intersection  
