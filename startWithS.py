str="hi swati do you like sweet"
str.lower()
s=str.split()
newstr=[]

for i in s:
    if i[0]=='s':
        newstr.append(i)
print(newstr)