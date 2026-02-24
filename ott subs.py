print('''Available platforms
1. Netflix - Rs.499
2. Amazon Prime - Rs.399
3. Disney+ Hotstar - Rs.299
4. AHA - Rs.199
5. Zee5 - Rs.149''')

amt = 0

print("How many OTT platforms do you want to select (1/2/3):")
ott = int(input())

if ott > 3:
    print("You can select only three at a time.")
else:
    for i in range(ott):
        print("Enter your choice:")
        ch = int(input())

        if ch == 1:
            amt += 499
        elif ch == 2:
            amt += 399
        elif ch == 3:
            amt += 299
        elif ch == 4:
            amt += 199
        elif ch == 5:
            amt += 149

    if ott == 1:
        dis = 0
    elif ott == 2:
        dis = 0.30
    else:
        dis = 0.40

    dis_amt = amt * dis
    amt_after = amt - dis_amt
    gst = amt_after * 0.20
    final_amt = amt_after + gst

    print("Bill Summary")
    print("No of OTT selected:", ott)
    print("Base amount:", amt)
    print("Discount amount:", dis_amt)
    print("GST amount:", gst)
    print("Final payable amount:", final_amt)