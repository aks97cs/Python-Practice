''' 
    @created by Anuj Kumar Singh
    example for module inheritance 
'''
import newmod
class mod_inherit(newmod.sum):
    def __init__(self):
        self.color = "red"
if __name__ == '__main__':
    x = mod_inherit()
    x.res()

