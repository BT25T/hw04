for i in range(100):
    num = i+1
    s_num = str(num)
    five = False
    three = False
    for digit in s_num:
        if digit == '5':
            five = True
        if digit == '3':
            three = True
    if num % 15 == 0 or num == 35 or num == 53:
        print("FizzBuzz")
    elif num % 5 == 0 or five == True:
        print("Buzz")
    elif num % 3 == 0 or three == True:
        print("Fizz")
    else:
        print(i+1)