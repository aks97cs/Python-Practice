def scope_test():
	def do_local():
		spam = "loacl spam"
	def non_local():
		nonlocal spam
		spam = "non local spam"
	def do_global():
		global spam
		spam = "global spam"
	spam = "testing spam"
	do_local()
	print("After local assignment spam is",spam)
	non_local()
	print("After non_local assignment of spam is ",spam)
	do_global()
	print("Do global assignment of spam is  :-",spam)

scope_test()
print("in global scope test spam is ",spam)