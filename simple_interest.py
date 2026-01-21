principal_amt = int(input("Enter the principal ammount : "))
time_taken = int(input("Enter time taken in years : "))
interest_rate = int(input("Enter the interest rate : "))
simple_interest = (principal_amt*time_taken*interest_rate)/100
total_amount = simple_interest+principal_amt
print("SIMPLE INTEREST : ",simple_interest)
print("Total amount : ",total_amount)
