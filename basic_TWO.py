
#Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).

def countdown(numberPlease):
    my_list = []
    for i in range(numberPlease, -1,-1):
        my_list.append(i)
    print(my_list)
# print(countdown(5))


# Print and Return - Create a function that will receive a list with two numbers.
#  Print the first value and return the second.

def twoInts(mine):
    print(mine[0])
    return(mine[1])
# print(twoInts([1,2]))


# First Plus Length - Create a function that accepts a list and 
# returns the sum of the first value in the list plus the list's length.

def sum_of_index_and_list(additup):
    return(additup[0] + len(additup))
# print(sum_of_index_and_list([1,5,9]))




# Write a function that accepts a list and creates a new list containing only 
# the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

def do_alot_of_stuff(do_alot):
    sum_of_second = 0
    newArr = []
    if len(do_alot)>=2:
        for i in range(len(do_alot)):
            if(do_alot[i]>do_alot[1]):
                sum_of_second+=1
                newArr.append(do_alot[i])
    else:
        return(False)
    print(sum_of_second)
    return(newArr)

# print(do_alot_of_stuff([5,2,3,2,1,4]))
# print(do_alot_of_stuff([5]))




# This Length, That Value - Write a function that accepts two integers
#  as parameters: size and value. The function should create and return a
#  list whose length is equal to the given size, and whose values are all 
# the given value.


def size_and_val(size, value):
    newArr = []
    for i in range(size):
        newArr.append(value)
    return(newArr)

# print(size_and_val(5,9))