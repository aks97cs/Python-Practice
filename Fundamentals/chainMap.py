'''
    @created by : Anuj Kumar Singh
    Understanding chainMap
'''
import collections
dic1  = {'name':'anuj','course':'b.tech'}
dic2 = {'roll_no':'1507710017','mobile_no':'8077427591'}
chain = collections.ChainMap(dic1,dic2)
#show all key mapping
# print(list(chain.maps))
print(chain.maps)
#show all key
print(list(chain.keys()))
#show all values
print(list(chain.values()))