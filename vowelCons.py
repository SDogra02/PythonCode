str="Hi Team what is gooing on"
vow=list(filter(lambda ch:ch.lower() in 'aeiou',str))
print("Len of vowel: ", len(vow))
con=str.replace(' ','')
print("len of consonent", len(con)-len(vow))
