class Rectangle():
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def Area(self):
        return self.width*self.length   
    def Perimeter(self):
        return (self.width+self.length)*2
    def display(self):
        print("-------------------")
        print("length : ", self.length)
        print("width : ", self.width)
        print("perimeter : ", self.Perimeter())
        print("area : ", self.Area())

class Parallelepipede(Rectangle):
    def __init__(self, length, width , height):
        Rectangle.__init__(self, length, width)
        self.height = height
        
    def volume(self):
        return self.length*self.width*self.height

a=int(input("Enter length : "))
b=int(input("Enter width : "))
c=int(input("Enter height: "))


newRectangle = Rectangle(a ,b )
newRectangle.display()
print("----------------------------------")
newParallelepipede = Parallelepipede(a , b , c)
print("volume : " , newParallelepipede.volume())