class base:
	def __init__(self):
		self.color = "red"
	y="fs"
class derived(base):
	def __init__(self):
		self.color = "red....."
x = derived()
print(x.color)