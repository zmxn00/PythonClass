class Triangle:
    numberOfSides = 3

    def __init__(self, a1, b1, c1):
        self.angle1 = a1
        self.angle2 = b1
        self.angle3 = c1

    def checkAngles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
        
Triangle = Triangle(90, 30, 60)
print(Triangle.checkAngles())