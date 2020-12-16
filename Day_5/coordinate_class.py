#defining a class for coordinate system

class Coordinate(object):
    #define the data attributes for an instance of the class Coordinate
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def __add__(self, other):
        x_coord = self.x + other.x
        y_coord = self.y + other.y
        return Coordinate(x_coord , y_coord)

    def __sub__(self , other):
        x_coord = self.x - other.x
        y_coord = self.y - other.y
        return Coordinate(x_coord, y_coord)

    def distance(self , other):
        '''
        (Coordinate) -> float
        Returns the distance between the current coordinate and the other coordinate.
        >>>Coordinate(2 , 1).distance(Coordinate(1 , 0))
        2
        '''
        x_dist = (self.x - other.x) ** 2
        y_dist = (self.y - other.y) ** 2
        return (x_dist + y_dist) ** 0.5


a = Coordinate(2 , 1)
print(a)
b = Coordinate(1 , 0)
print(b)
print(a.distance(b))
print(a + b)
print(a - b)