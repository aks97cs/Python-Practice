class test:
    def takeinput(self):
        self.name=input("Enter your name:")
        self.course=input("Enter your course:")
    def boom(self):
        self.name=input("Enter your name")
        self.course=input("enter your course")
    def display(self):
        print("Name:",self.name)
        print("Course:",self.course)



obj1=test()
obj1.takeinput()
obj1.boom()
obj1.display()
