# Write a recursive function to calculate the sum of first n natural numbers.

# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def factorial_recursive_sum(n):
    if n == 1 or n == 0:
        return 1
    return factorial_recursive_sum(n-1) + n

# f = factorial_iter(5)
f = factorial_recursive_sum(2)
print(f)