num = int(input("Enter a number: "))
s_num = str(num)
n = len(s_num)
count = 0
for i in range(n):
    count += int(s_num[i])
print(f"Digit sum: {count}")