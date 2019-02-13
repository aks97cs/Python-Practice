fh = open('data.txt')
for line in fh.readlines():
    print(line)
    print(type(line))