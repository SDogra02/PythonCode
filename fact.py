num=int(input("Enter num: "))
fact=1
if num<0:
    print("Enter positive integer")
elif num==0:
    print("1")
else:
    for i in range(1, num+1):
        fact=fact*i
    print(fact)