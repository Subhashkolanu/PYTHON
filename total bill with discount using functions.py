def total_amt(price,quantity,discount=0):
    total=price*quantity
    discount=total*discount/100
    final_amt=total-discount
    print("-----Bill reciept-----")
    if final_amt==total:
        print("Total amount :",total)
        print("Final amount :",final_amt)
    else:
        print("Total amount :",total)   
    if discount>0:
        print("Discount :",discount)
        print("Final ammount :",final_amt)
p=float(input("Enter the price : "))
q=int(input("Enter the quantity : "))
total_amt(p,q)
total_amt(p,q,discount=10)