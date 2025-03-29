class Point(object):
    """`x`: x-coordinates; `y`: y-coordinates"""
    def __init__(self, x, y):
        super(Point, self).__init__()

        self.__x = x
        self.__y = y
        
    def get(self): 
        return self.__x, self.__y

point = Point(-67, 148)
print(point.get())