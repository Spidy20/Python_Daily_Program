# Day - 5 - 26/07/2021
# Type - Basic Programming
# Program - Print the Fibonacci series for n th terms
# Explanation - For 5 th terms , fibonacci series will be like
# 0,1,1,2,3,5,8,13,21

def fibonacci_series(number_of_terms):
    # first two terms
    n1, n2 = 0, 1
    count = 0
    fibonacci = []
    if number_of_terms <= 0:
       print("Please enter a positive integer")
    elif number_of_terms == 1:
       print("Fibonacci sequence upto",number_of_terms,": 0" )
    else:
       print("Fibonacci sequence:")
       while count < number_of_terms:
           fibonacci.append(n1)
           print(n1,n2)
           total = n1 + n2
           print(total)
           # update values
           n1 = n2
           n2 = total
           count += 1
    return fibonacci

fib = fibonacci_series(7)
print(fib)