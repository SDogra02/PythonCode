a=int(input("Enter any number: "))
b=int(input("Enter any number: "))
c=int(input("Enter any number: "))
sum=a+b+c
if sum<=21:
    print(sum)
elif (sum>21) and (a==11) or (b==11) or (c==11):
    newval= sum-10
    print(newval)
else:
    print("Bust")
  