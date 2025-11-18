# Write a program to print no. from 1 to n using recursion
n = int(input("Enter value of n: "))

def print_numbers(i, n):
    if i > n:     
        return
    print(i)
    print_numbers(i + 1, n)  
print_numbers(1, n)

#Write a program to print n to 1

n = int(input("Enter value of n: "))
def print_reverse(i):
    if i == 0:   # base condition
        return
    print(i)
    print_reverse(i - 1)   # recursive call

print_reverse(n)

# write a recursive function to find the Nth fibonacci no. 

n = int(input("Enter n: "))
def fibonacci(n):
    if n == 0:
        return 0   # Base Case
    if n == 1:
        return 1   # Base Case
    return fibonacci(n-1) + fibonacci(n-2)  # Recursive Call

print("Fibonacci number:", fibonacci(n))

# Write a program to find the sum of digit of a given no. using recursion
num = int(input("Enter a number: "))
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

result = sum_of_digits(num)
print("Sum of digits =", result)

#write a recursive function to reverse a string
text = input("Enter a string: ")
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

print("Reversed string:", reverse_string(text))

