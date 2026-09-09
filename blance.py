intial_balance = float(input("Enter Intial Balance: "))
deposit = float(input("Enter Amount to Deposit: "))

blance = intial_balance + deposit
withdraw_amt = float(input("enter the withdraw amt"))
new_blance = blance-withdraw_amt
                   
print("Intial Balance: ", intial_balance)
print("Amount to Deposit: ", deposit)
print("your balance is :", blance)  
print("your new blanvce: ",new_blance)
