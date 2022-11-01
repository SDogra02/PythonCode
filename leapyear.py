year=int(input("Enter any year: "))
if year%100!=0:
    print("its a leap year")
elif year%4==0:
    print("its a leap year")
else:
    print("Not a leap year")