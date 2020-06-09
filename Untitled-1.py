class Circle:
    radius=0

    def __init__(self,r):
        self.radius= r
    
    def circumfrence(self):
        return 3.141 * 2 *self.radius

circleA=Circle(1)

print("Circle A circumfrance "+ str(circleA.circumfrence()))