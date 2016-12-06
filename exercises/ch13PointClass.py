class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)
        
    def distanceFromPoint(self, otherPoint):
        """Distant between itself and the mentioned point"""
        return (((self.x-otherPoint.x) ** 2) + 
                ((self.y-otherPoint.y) ** 2)) ** 0.5
    
    def reflect_x(self):
        return Point(self.x, -self.y)
    
    def get_line_to(self, otherPoint):
        rise = otherPoint.y - self.y
        run = otherPoint.x - self.x
        m = rise/run
        b = -self.x * m
        return (m, b)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        

