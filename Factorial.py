#Finding Factorial of a number using Recursion

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

ans = int(input("Enter a number to find factorial: "))
print(f"The Factorial of {ans} is {factorial(ans)}")