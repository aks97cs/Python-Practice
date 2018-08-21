class wxy:
	global a #making "a" a global variable
	a=5
	def show(self):
		global a #way to access a global variable in a method
		a = a*7
		print(a) #Output = 35
def main():
	obj = wxy() #making an object of class wxy
	obj.show()
if __name__ == '__main__':
	main()