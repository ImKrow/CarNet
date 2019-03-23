

class Node(object):


    def __init__(self, x, y, min_speed, max_speed):
        self.x = x
        self.y = y
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.location = [x,y]


    def get_location(self):
        return [self.x,self.y]

    def get_current_speed(self):
        return self.max_speed


