print("Enter your height in feet : ")
height=float(input())
if height>=3:
    print("You can ride on the horse.")
    print("Enter your age :")
    age=int(input())
    if age<=12:
        print('Your fare is ₹150')
    elif age>=13 and age<=18:
        print('Your fare is ₹250')
    else:
        print("Your fare is ₹500")
else:
    print('You cannot ride on horse. Thank you')