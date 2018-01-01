Str1=input("enter the string1:")
Str2=input("enter the string2:")
Merge=""
for i in Str1:
    if i.isupper():
        Merge=Merge+i
    else:
        pass
for i in Str2:
    if i.isupper():
        Merge=Merge+i
    else:
        pass
print(Merge)
