Str=input("enter the string:")
count1=0
count2=0
count3=0
count4=0
for i in Str:
    if (i=='a' or i=='A'):
        count1=count1+1
    elif(i=='b' or i=='B'):
        count2=count2+1
    elif(i=='c' or i=='C'):
        count3=count3+1
    elif(i=='g' or i=='G'):
        count4=count4+1
if(count1>count2 and count3 and count4):
    print("count1 is largest")
elif(count2>count1 and count3 and count4):
    print("count2 is largest")
elif(count3>count1 and count2 and count4):
    print("count3 is largest")
else:
    print("count4 is largest")
