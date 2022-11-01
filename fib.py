def fib(num):
    num1, num2 = 0, 1
    if num>0:
        for i in range(num):
            print(num1, end=" ")
            res = num1 + num2
            num1 = num2
            num2 = res
    else:
        print("Enter a positive integer")
fib(4)