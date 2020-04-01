a=[]
for i in range(0,19):
    num = int(input("Enter value: "))
    a.append(num)
print(a)

list = a

b=set(list)

for i in b:
    list.count(i)
    print(str(i)+"-->",list.count(i))
    
