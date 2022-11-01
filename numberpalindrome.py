num=121
tempnum=num
rev=0

while tempnum>0:
    digit=tempnum%10
    rev=rev*10+digit
    tempnum=tempnum//10
if rev==num:
    print("number is palindrome")
else:
    print("number is not palindrome")