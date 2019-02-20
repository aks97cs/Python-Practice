'''
    @created by Anuj Kumar Singh
    module to import in mod_inherit.py
    Note : contructure are not inherited 
'''
class sum:
    def __init__(self):
        self.num1 = 10
        self.num2 = 20
    def res(self):
        self.num1 = 10
        self.num2 = 20
        self.result= self.num1+self.num2
        print(self.result)