class Box:
    def  __init__(self, l, h, d):
        self.l = l
        self.h = h
        self.d = d

    def __str__(self):
        return f"{self.l}, {self.h}, {self.d}"
    
    def setLength(self, l):
        self.l = l
        
    def getLength(self):
        return self.l
    
    def setHeight(self, h):
        self.h = h
    
    def getHeight(self):
        return self.h
    
    def getDepth(self):
        return self.d
    
b1 = Box(100, 100, 100)
print(b1)
print("상자의 부피는", b1.getLength() * b1.getHeight() * b1.getDepth())