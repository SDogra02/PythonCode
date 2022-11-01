n=int(input("Enter any number: "))
for i in range(1,n+1):
    if n>0:
        for j in range(2,i):
            if (i%j)==0:
                break
        else: 
            print(i)
    
