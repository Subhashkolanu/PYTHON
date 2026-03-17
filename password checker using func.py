def check_password(p):
    if len(p) < 6:
        return "Weak"
    elif any(c.isdigit() for c in p) and any(c.isalpha() for c in p):
        return "Strong"
    else:
        return "Medium"

password = input("Enter password: ")
print("Strength:", check_password(password))