class hinhchunhat():
    def __init__(self, d, r):
        self.dai = d
        self.rong  = r

    def DientichHCN(self):
        return self.dai*self.rong

show = hinhchunhat(int(input()), int(input()))
print(show.DientichHCN())
