class Point:
    count = 0
    def __init__(self, x , y):
        self.x = x
        self.y = y
        Point.count += 1
    def show(self):
        print(f"({self.x}, {self.y})")


class Line:
    count = 0
    def __init__(self, p1 , p2):
        self.p1 = p1
        self.p2 = p2
        Line.count += 1
    def show(self):
        return f"({self.p1.show()}, {self.p2.show()})"
    @classmethod
    def how_many(cls):    
        return cls.count


l1 = Line(Point(5,6), Point(2,6))
l2 = Line(Point(4,8), Point(4,10))
l3 = Line(Point(1,7), Point(6,3))

l1.show()
l2.show()
l3.show()


print (Point.count)
print (Line.count)
print (Line.how_many())

@staticmethod
def is_horizontal(y1, y2):
    if y1 == y2:
        return True
    else:
        return False

@staticmethod
def  is_vertical(x1 , x2):
    if x1 == x2:
        return True
    else:
        return False
    






