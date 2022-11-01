str = "200 plus 500 equal to 700"
str1=str.split()

print(str1, type(str1))
sum=0
for i in str1:
    if(i.isdigit()):
        sum=sum+int(i)
    else:
        continue
print(sum)