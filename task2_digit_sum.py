num = int(input("Enter a number: "))
count = 0
if num < 0 :
    print("Invaild number")
else:
    while num != 0:
        count += num%10
        num = num // 10
    print(f"Digit sum: {count}")