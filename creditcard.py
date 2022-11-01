def cc(s1):
    s=list(s1)
    new=[]
    for i in range(len(s)):
        if(i<len(s)-4):
            new.append('*')
        else:
            new.append(s[i])
    return new
card=input("Enter any number: ")
print(''.join(cc(card)))