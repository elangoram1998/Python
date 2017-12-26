Employee_Id=int(input("Employee ID:"))
Basic_Salary=int(input("Basic salary of an employee:"))
Allowance=int(input("Allowance of an employee:"))
Gross_Salary=Basic_Salary+Allowance
if Gross_Salary <=5000:
    print("gross salary is:",Gross_Salary)
elif Gross_Salary in range(5001,10001):
    Income_Tax=Gross_Salary*10/100
    Net_Salary=Gross_Salary-Income_Tax
    print("net salary is:",Net_Salary)
elif Gross_Salary in range(10001,20001):
    Income_Tax=Gross_Salary*20/100
    Net_Salary=Gross_Salary-Income_Tax
    print("net salary is:",Net_Salary)
else:
    Income_Tax=Gross_Salary*30/100
    Net_Salary=Gross_Salary-Income_Tax
    print("net salary is:",Net_Salary)
