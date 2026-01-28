principal_amt = int(input("Enter the principal amount : "))
interest_rate = int(input("Enter the interest rate : "))
time_taken = int(input("Enter time taken in months : "))
simple_interest = (principal_amt*time_taken*interest_rate)/100
total_amount = simple_interest+principal_amt
print("SIMPLE INTEREST for Every month: ",(principal_amt*interest_rate)/100)
print("SIMPLE INTEREST for the time: ",simple_interest)
print("Total amount to be repayed : ",total_amount)
