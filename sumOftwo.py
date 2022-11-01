def sumOfTwo(a,b,c):
    l = len(a)
    for i in range(l):
        if a[i] + b[i] == c:
            print('true',a[i]+b[i],c)
        else:
            print('false',a[i]+b[i],c)

a =[1,2,3]
b=[10,20,30]
c = 33
sumOfTwo(a,b,c)
