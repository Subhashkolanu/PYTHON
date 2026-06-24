num = 10
binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num = num // 2

print(binary)