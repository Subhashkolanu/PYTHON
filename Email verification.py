''' A college admission system allows students to register using specific email domains. The system must validate the user's email address before completing the registration process.
An email address is considered valid only if:
•	It contains exactly one "@" symbol.
•	It does not contain any spaces.
•	It ends with any one of the following domains:
@college.edu
@gmail.com
@yahoo.co.in
If the email satisfies all the above conditions, the program should display:” valid email,” otherwise, “not a valid email.”
'''
email=input("Enter your Email : ")
at=email.count('@')
space=" " in email
domain=email.endswith(('@yahoo.co.in',"@gmail.com","college.edu"))
if at == 1 and not space and domain:
    print('Valid email')
else:
    print('Invalid Email')