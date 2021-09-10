from tkinter import*
class TK_extended(Tk):
    def __init__(self, master , title):
        self.master = master
        self.title = title
    def create(self):
        self.master = Tk()
        self.master.title(self.title)              
    def resize(self, width , height):
        self.master.geometry("%dx%d"%(width , height))

    def generate(self):
        self.master.mainloop() 
        
def main():   
    root = TK_extended("root" , "Title")
    root.create()
    root.resize(500 , 500)
    root.generate()

if __name__ == '__main__':
    main()