# Day - 2 - 14/07/2021
# Type - Basic Programming
# Program - Check given number is Armstrong or not
# 153 = 1*1*1 + 5*5*5 + 3*3*3 = 153 // 153 is an Armstrong number.

def armstrong_num_checker(number):
    # initialize answer = 0
    ans = 0
    # For find the sum of the cube of each digit
    temp = number
    ## To find the length of the number, so we can set the power of that length
    ln = int(len(str(number)))

    # Now we are going into While Loop for
    while temp>0: # IF DIGIT 3 ** 3 0
        digit = temp % 10
        print('Digit we are goinng to do the Power: ',digit)
        ans += digit ** ln
        print('Total Answer : ',ans)
        temp //= 10
        print('Remaining number: ',temp)
    # if answer == original number then it's armstrong number
    if number == ans:
        print(number, "is an Armstrong number")
    else:
        print(number,  "is not an Armstrong number")

armstrong_num_checker(548834)