Employee_Id=int(input("Employee ID:"))
Basic_Salary=int(input("Basic salary of an employee:"))
Allowance=int(input("Allowance of an employee:"))
Gross_Salary=Basic_Salary+Allowance
if Gross_Salary > 10000:
    Income_Tax=Gross_Salary*20/100
    Net_Salary=Gross_Salary-Income_Tax
    print("net salary is:",Net_Salary)
else:
    print("gross salary is:",Gross_Salary)
