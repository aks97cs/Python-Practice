class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("name is {} and age is {}".format(self.name,self.age))


class teacher(person):
    def print(self,name,age):
     person.__init__(self,name,age)
