class Node(object):

    def __init__(self, x, y, minSpeed, maxSpeed):
        self.x = x
        self.y = y
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.location = [x,y]

    #
    def get_location(self):
        print(1)
        return [self.x,self.y]


print("hi")