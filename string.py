str=input("Enter any string: ")

for i in range(0, len(str)):
    count=1
    for j in range(i+1, len(str)):
        if str[i] == str[j] and str[i]!=0:
            count=count+1
            str=str[:j] + '0' + str[j+1:]
    if(count>1 and str[i]!='0'):
        print(str[i], count)


str="Tutorial point"
dup=[]
for char in str:
    if str.count(char)>1:
        if char not in dup:
            dup.append(char)
print(dup)

def hasDuplicates(s):
    for c in s:
        if s.count(c) > 1:
            print(c)
hasDuplicates("Hello")