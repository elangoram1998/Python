Str=input("enter the string:")
Punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s=""
for char in Str:
    if char not in Punctuation:
        s=s+char
    else:
        pass
print(s)
        
