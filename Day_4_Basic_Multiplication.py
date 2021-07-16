# Day - 4 - 16/07/2021
# Type - Basic Programming
# Program - Print the multiplication table for given number
# Explanation - Logic is very simple, if number is 2 then 2*i upto N

def multiplication_table(number,table_range = 10):
    for i in range(1,table_range+1):
        print(number, '*',i,'=',number*i)

multiplication_table(19)