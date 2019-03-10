'''
Eploring dictionary
@mutable
'''
D = {'f_name':'Anuj'}
print(D['f_name'])
#zipping
details = dict(zip(['name','course','domain'],['anuj','b.tech','web app']))
# details = 
details = dict(zip(['name','course','domain'],['anuj','b.tech','web app']))

print(details)
for i in details:
    print(i,details[i])
    # print(details[i])

food = {'pizza': 324, 'sandwich': 78, 'hot dog': 90}
food_list=list(food.values())
print(food_list)