Str=input("Enter the string:")
count=0
for i in Str:
    if i.isupper():
        count+=1
    else:
        pass
print("No of capital letters:",count)
