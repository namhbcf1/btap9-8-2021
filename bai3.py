class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)
    
class Student(Person):
    def __init__(self, name , age , section):
        super().__init__(name, age)
        self.section = section
    
    def displayStudent(self):
        print("Student name : ", self.name)
        print("Student age = ", self.age)
        print("Student section = ", self.section)
    
def main():
    a=str(input("Enter Person name: "))
    b=int(input("Enter Person age = "))
    c=str(input("Enter Student name : "))
    d=int(input("Enter Student age = "))
    e=str(input("Enter Student section : "))
    Per = Person("a", b)
    Per.display()
    print("-------------------------------")
    Stu = Student(c, d , e)
    Stu.displayStudent()

if __name__ == '__main__':
    main()

