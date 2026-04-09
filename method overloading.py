def Product(*t):
    p=1
    for ele in t:
        p=p*ele
    print(p)

Product(4,5)
Product(4,5,6)
Product(4,5,6,7)

