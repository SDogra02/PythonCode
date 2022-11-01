str="abcva"
fstr=0
lstr=len(str)-1
while fstr<lstr:
    if str[fstr]!=str[lstr]:
        print("string is not palindrome")
        break
    fstr=fstr+1
    lstr=lstr-1  
else:
    print("string is palindrome")
