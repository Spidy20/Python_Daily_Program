# Day - 3 - 15/07/2021
# Type - Basic Programming
# Program - Print the all prime numbers in range.
# Explanation - Assume that 10-20 is the range, Here 11,13,17,19 are the prime numbers.

def prime_number_finder(start,end):
    prime_number = []
    for i in range(start, end + 1):
        if i > 0:
            print(i)
            for j in range(2, i):
                if (i % j == 0):
                    print(i,j)
                    break
            else:
                prime_number.append(i)
    return prime_number,"Total Prime Numbers are: "+ str(len(prime_number))

test,q = prime_number_finder(1,15)
print(test,q)