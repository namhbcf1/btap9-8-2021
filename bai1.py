class hinhchunhat():
    def __init__(self, d, r):
        self.dai = d
        self.rong  = r

    def DientichHCN(self):
        return self.dai*self.rong

a=int(input("Enter length of rectangle: "))
b=int(input("Enter width of rectangle: "))

show = hinhchunhat(a, b)
print(show.DientichHCN())
