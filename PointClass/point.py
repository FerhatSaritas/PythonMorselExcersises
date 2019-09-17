class Point:
    x = 0
    y = 0
    z = 0

    def __init__(self, x:int, y:int, z:int):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return 'Point(x='+str(self.x)+', y='+str(self.y)+', z='+str(self.z)+')'

    def __repr__(self):
        return 'Point(x='+str(self.x)+', y='+str(self.y)+', z='+str(self.z)+')'
    
    def __add__(self, x):
        return Point(self.x+x.x, self.y+x.y, self.z+x.z)
    
    def __sub__(self, x):
        return Point(self.x-x.x, self.y-x.y, self.z-x.z)
    
    def __mul__(self, x):
        return Point(self.x*x, self.y*x, self.z*x)

    def __rmul__(self, x):
        return Point(self.x*x, self.y*x, self.z*x)

    def __iter__(self):
        yield from [self.x, self.y, self.z]

    def __ne__(self, x):
        if self.x != x.x or self.y != x.y or self.z != x.z:
            return True
        else:
            return False
    def __eq__ (self, x):
        if self.x == x.x and self.y == x.y and self.z == x.z:
            return True
        else:
            return False