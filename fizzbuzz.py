n=int(input("enter the num"))

for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        i = ("fizzbuzz")
    elif(i%3==0):
        i = ("fizz")
    elif(i%5==0):
        i = ("buzz")
    print(i)
