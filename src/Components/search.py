lists = []
with open("output.txt", "r") as f:
    line = f.readline()
    while line:
        line = line.strip()
        line = line.split(' ')
        temp = []
        temp.append(line[1].strip())
        temp.append(line[2].strip())
        temp.append(line[0].strip())
        lists.append(temp)
        line = f.readline()

#print(lists)
e1 = input()
e2 = input()

for item in lists:
    if (e1 == item[0] and e2 == item[1])  or (e1 == item[1] and e2 == item[0]): 
        print(item[0], item[1])
        print(item[2])
        
