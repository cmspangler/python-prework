#Question 1:
#Write a function to print "hello_USERNAME" USERNAME is the input of the function

def hello_name(user_name):
    
    print("Hello_" + user_name.upper())

hello_name('chad')


#Question 2:
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for num in range(1, 100):
        if num % 2 !=0:
            print(num, end=" ")

first_odds()

#Question 3:
#Write a python function, max_num_in_list to return the max number in a given list. 

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max= a
    return max
print(max_num_in_list ([1, 14, -8, 0]))


# Question 4:
# Write a Python function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100 unless it is 400.
# The return should be a boolean type. (true/ false)

def is_leap_year(a_year):
    leap = False
    if a_year % 400 == 0:
        leap = True
    elif a_year % 4 == 0 and a_year != 100:
        leap = True
    return leap

a_year = int(input())
print(is_leap_year(a_year))



#def is_leap_year(a_year)

# Question 5:
# Write a function to check to see if all numbers in a list are consecutive numbers. 
# Return should be boolean

def is_consecutive(a_list):
    if len(a_list) < 1:
        return False
    min_value = min(a_list)
    max_value = max(a_list)
    if max_value - min_value + 1 == len(a_list): 
        for i in range(len(a_list)):
            if a_list [i] < 0:
                j = -a_list [i] - min_value
            else:
                j = a_list[i] - min_value
                if a_list[j] > 0:
                    a_list[j] = -a_list[j]
                else:
                    return False
            return True
        return False
a_list = [1, 2, 3, 4, 5]
print(is_consecutive(a_list))
