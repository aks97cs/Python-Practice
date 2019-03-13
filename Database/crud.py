import sqlite3
def menu():
	print("*********** OPERATION TO PERFORM **********")
	print("1.Insert")
	print("2.Show")
	print("3.Retrive")
	print("4.Update")
	print("5.Delete")
	global ch
	ch = input("Enter your choice = ")
	if ch =='1':
		insert(db)
	elif ch == '2':
		Show(db)
	elif ch == '3':
		Retrive(db)
	elif ch == '4':
		Update(db)
	elif ch == '5':
		Delete(db)
	
def insert(db):
	print("************** INSERT VALUE ******************")
	global name
	global roll_no
	global course
	name = input("Enter your name  = ")
	roll_no = input("Enter your roll mo = ")
	course = input("Enter the course you have opt = ")
	db.execute('insert into test (name,roll_no,course) values (?,?,?)',[name,roll_no,course])
	db.commit()
	menu()
def Show(db):
	print("****************** SHOW VALUE *******************")
	cursor = db.execute('select * from test')
	for row in cursor:
		print(row[0],row[1],row[2])
	menu()
def Retrive(db):
	print("**************** SEARCH VALUE *****************")
	global search_roll_no
	search_roll_no = input("Enter the roll no to search = ")
	cursor = db.execute('select * from test')
	for row in cursor:
		#print("row = ",row[1])
		if(row[1] == search_roll_no):
			print(row[0],row[1],row[2])
			break
		else:
			print("Roll no does not exist")
	menu()
def Update(db):
	print("******************** UPDATE VALUE ****************")
	update_roll_no = input("Enter the roll no whoes value you want to update = ")
	print("1.Update Name")
	print("2.Update roll no")
	print("3.Update Course")
	global x
	x = input("Enter your choice = ")
	if x =='1':
		newname = input("Enter the new name = ")
		db.execute('update test set name = ? where roll_no = ?',(newname,update_roll_no,))
		print("Sucessfully updated !!")
		db.commit()
		menu()
	elif x == '2':
		newrollno =input("Enter your new roll no = ")
		db.execute('update test set roll_no = ? where roll_no = ?',(newrollno,update_roll_no))
		print("Sucessfully updated !!")
		db.commit()
		menu()
	elif x == '3':
		newcourse = input("Enter your new course = ")
		db.execute('update test set course = ? where roll_no = ?',(newcourse,update_roll_no))
		print("Sucessfully updated !!")
		db.commit()
		menu()
def Delete(db):
	print("ok")





def main():
	print("******* CREATING TABLE *********")
	global db
	db = sqlite3.connect('test.db')
	#db.execute('drop table if exists test')
	#db.execute('create table test (name text,roll_no text,course text)')
	menu()
if __name__ == '__main__':main()