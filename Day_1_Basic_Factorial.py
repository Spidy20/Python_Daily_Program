# Day - 1 13/07/2021
# Type - Basic Programming
# Program Factorial of Number

# Example : Factorial of 4 is 4*3*2*1 = 24
# 3?? 3*2*1 = 6   4?  4*3*2*1 = 24
def factorial_of_num(number):
    fact = 1
    # Check if the number is negative, positive or zero
    if number < 0:
        print("Factorial of negative number is not possible")
    elif number == 0:
        print("The Factorial of 0 is 1")
    else:
        for i in range(1, number + 1):
            print(str(fact)+' =',str(fact),'*',str(i))
            fact = fact * i
            ''' Loop explanation

            fact is 1, we have initialized
            now
            if we want to find factorial for 4
            then it should be like
            1 = 1*1  - 1st Iteration
            1 = 1*2  - 2nd Iteration
            2 = 2*3  - 3rd Iteration
            6 = 6*4  - 4th Iteration
            24 -> Loop will be end

            '''
        print(fact)
        print("The factorial of", number, "is", fact)

n = int(input("Enter the number: "))
factorial_of_num(n)