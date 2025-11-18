def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n, end=" ")
N = int(input("enter a number : "))

print_numbers(N)
