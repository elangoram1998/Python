Number_of_Hours=int(input("enter the hours worked:"))
Pay_Rate_per_Hour=int(input("enter the pay rate:"))
No_of_Weeks=int(input("no of weeks in a month:"))
if Number_of_Hours>=40:
    Monthly_pay=Number_of_Hours*Pay_Rate_per_Hour*No_of_Weeks
    print("Monthly pay of an employee:",Monthly_pay)
else:
    print("low time work:")
