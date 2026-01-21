#1. Write a Python program using function that calculates the factorial of a given number n (n!) using both a for loop and a while loop.
# # Example:
# #    Input: n = 4
# # Output: 24
# # Explanation: (4! = 4 × 3 × 2 × 1 = 24)
#
# # Solution
# # # Solution using for loop
# def get_factorial_using_for_loop(num):
#     ans = 1
#     for i in range(1, num + 1):
#         ans *= i
#     return ans
#
# # Solution using for while
# def get_factorial_using_while_loop(num):
#     ans = 1
#     i = 1
#     while i <= num:
#         ans *= i
#         i += 1
#     return ans
# # Calling Functions
# num = 4
# print(f"Factorial of {num} using for loop =  {get_factorial_using_for_loop(num)}")
# print(f"Factorial of {num} using while loop= {get_factorial_using_while_loop(num)}")
from multiprocessing.reduction import duplicate
from tkinter.messagebox import YESNO


#=========================

# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)

# def factorial_number(n):
#     #num = int(input("Enter a number: "))
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
# aa= factorial_number(8)
# print(aa)

# 2. Write a Python program that finds and prints all the prime numbers between 1 and N using both a for loop and a while loop.
# Example :
# Input:  N = 10
# Output: 2 3 5 7
# Explanation: (Prime numbers between 1 and 10 are 2, 3, 5, and 7)
#
# Solution
# # Solution Using a for loop

# def get_prime_numbers_using_for(num):
#     list_of_prime_numbers = []
#     for i in range(2, num + 1):
#         is_prime_number = True
#         for j in range(2, i):  # Check all numbers from 2 to i-1
#             if i % j == 0:
#                 is_prime_number = False
#                 break
#         if is_prime_number:
#             list_of_prime_numbers.append(i)
#     return list_of_prime_numbers
# #
#
# # # Solution Using a while loop
# def get_prime_numbers_using_while(num):
#     list_of_prime_numbers = []
#     i = 2
#     while i <= num:
#         is_prime_number = True
#         for j in range(2, i):  # Check all numbers from 2 to i-1
#             if i % j == 0:
#                 is_prime_number = False
#                 break
#         if is_prime_number:
#             list_of_prime_numbers.append(i)
#         i += 1
#     return list_of_prime_numbers
#
# # Calling/executing functions
# num = 10
# print(f"Prime numbers between 1 and {num} using for loop: {get_prime_numbers_using_for(num)}")
# print(f"Prime numbers between 1 and {num} using while loop: {get_prime_numbers_using_while(num)}")

#====================================================================================================
#practice by me
#Write a Python program that finds and prints all the prime numbers between 1 and N using both a for loop and a while loop.
#for loop

#easy logic
#if number is divisible and by 1 and itself
#2nd should be grater than 1
# we need to divide that number strating from itself till the given range (n-1)

# num = int(input("Enter a number: "))
# if num <=1:
#     print(f"{num} is not a prime number")
# elif num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(f"{num} is a not prime number")
#             print(f"{i} is factor of {num}")
#             break
#     else:
#         print(f"{num} is  a prime number")


#====================================================================================================
# 3. Write a Python program that counts the number of digits in a given number using both a for loop and a while loop.
# Example :
# Input: n = 12345
# Output: 5
# Explanation: (Number of digits in 12345 is 5)
#
# Solution
# # Function to count digits using a for loop
# def count_digits_using_for_loop(num):
#     count_of_digits = 0
#     for digit in str(num):  # Convert number to string and iterate through each character
#         count_of_digits += 1
#     return count_of_digits
#
# # Function to count digits using a while loop
# def count_digits_using_while_loop(num):
#     count_of_digits = 0
#     while num != 0:
#         num = num // 10  # Remove the last digit of the number
#         count_of_digits += 1
#     return count_of_digits
#
# # Input
# num = 12345
#
# # Calling the functions
# print("Number of digits using for loop):", count_digits_using_for_loop(num))
# print("Number of digits using while loop):", count_digits_using_while_loop(num))

#====================================================================================================
# practice. Write a Python program that counts the number of digits in a given number using both a for loop and a while loop.

# def count_digits():
#     digit= 12345
#     count=0
#     for i in str(digit):
#         count+=1
#     return count
# aa=count_digits()
# print(aa)

# digit= "12345"
#     count=0
#     for i in digit:
#         count+=1
#     print(count)

#====================================================================================================
# 4. Write a Python program that calculates the sum of the first N natural numbers (1 + 2 + 3 + ... + N) using both a for loop and a while loop.
# Example
# Input: N = 5
# Output: 15
# Explanation: (Sum of 1 + 2 + 3 + 4 + 5 = 15)
#
# Solution
# # Function to calculate sum using a for loop
# def sum_of_n_natural_number_using_for_loop(num):
#     total = 0
#     for i in range(1, num+1):
#         total += i
#     return total
#
# # Function to calculate sum using a while loop
# def sum_of_n_natural_number_using_while_loop(num):
#     total = 0
#     i = 1
#     while i <= num:
#         total += i
#         i += 1
#     return total
#
# # Taking inputs dynamically
# num = int(input("Enter a number : "))
#
# # Output
# print("Sum of natural number using for loop:", sum_of_n_natural_number_using_for_loop(num))
# print("Sum of natural number  using while loop:", sum_of_n_natural_number_using_while_loop(num))

#====================================================================================================
# practice 4. Write a Python program that calculates the sum of the first N natural numbers (1 + 2 + 3 + ... + N) using both a for loop and a while loop.

# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num + 1):
#     sum += i
# print(sum)
#====================================================================================================
#
# 1.	Write a function to return the grade based on percentage
#
# Solution:
#
# def getGrade(perc):
#     if perc < 35:
#         grade ="Fail"
#     elif perc >= 35 and perc <= 50:
#         grade = "Third div"
#     elif perc >50 and perc<65:
#         grade = 'Second div'
#     else:
#         grade = "First div"
#     return grade
# perc = input("Enter the percetage :")
# print("Your garde is : ",getGrade(int(perc)))



# def marks_of_student(marks):
#     if marks >= 70:
#         print("Your grade is A")
#     elif marks >= 60:
#         print("Your grade is B")
#     elif marks >= 30:
#         print("Your grade is C")
#     elif marks >= 20:
#         print("Your grade is D")
#     else:
#         print("Your grade is F")
# aa=marks_of_student(10)
# print(aa)

#====================================================================================================

# 2.	Write a function that return a list of common elements from two different sets
#
# Solution:
# def findCommonElement(set1, set2):
#     set3 = set1 & set2
#     return set3
#
# set1 = {1,2,3,4,5}
# set2 = {1,4,5,8,9}
# print(findCommonElement(set1,set2))

# def common_list(set1, set2):
#     set3=[]
#     for i in set1:
#         if i in set2:
#             set3.append(i)
#     return set3
#
# set1 = (1,2,3,4)
# set2 = (3,4,5,6,7)
# aa= common_list(set1,set2)
# print(aa)

# set1 = (1,2,3,4)
# set2 = (3,4,5,6,7)
# set3=[]
# for i in set1:
#     if i in set2:
#         set3.append(i)
# print(set3)
#====================================================================================================

# 3.	Convert a String to a List of Characters

# #Solution:
# def convertStringToList(s):
#     return list(s)
# s = input("Enter a string : ")
# print(convertStringToList(s))

# str = input("enter the string :")
# list1 = list(str)
# print(list1)
# print(type(list1))

#====================================================================================================

#4.	Write a function to check if list contains any duplicate element and return “Yes” or “No” as application

# Check if my List contains any duplicate element
# Solution:
# def checkDuplicateInList(lst):
#     set1 = set(lst)
#     if(len(set1) == len(lst)):
#         return False
#     else:
#         return True
#
# lst = [1,2,3,4,5,20,1]
# ans = checkDuplicateInList(lst)
# print(ans)


#this
# l1=[11,11,2,3,44,44,5]
# set1=set(l1)
# if len(set1)==len(l1):
#     print("not duplicated")
# else:
#     print("duplicated")



# def duplicate_in_list(l1):
#     set1=set(l1)
#     if len(set1)==len(l1):
#         return False
#     else:
#         return True
#
# l1=[11,11,2,3,44,44,5]
# aa= duplicate_in_list(l1)
# print(aa)

#====================================================================================================

# 5.	Given a list, write a function that provide the occurrence of element against each element in the list.
# e.g. List = [1,2,3,4,5,1,3]
#    Expected Output:
#     1: 2
#     2:1
#     3: 2
#     4: 1
#     5: 1
#
# Solution: def count_elements(input_list):
#     counts = {}
#     for element in input_list:
#         if element in counts:
#             counts[element] += 1
#         else:
#             counts[element] = 1
#     return counts
#
# # Example usage:
# my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
# result = count_elements(my_list)
# print(result)

# List1 = [1,2,3,4,5,1,3]
# list2={}
# for i in List1:
#     if i in list2:
#         list2[i]+=1
#     else:
#         list2[i]=1
# print(list2)

# def occurance_count(List1):
#     list2 = {}
#     for i in List1:
#         if i in list2:
#             list2[i] += 1
#         else:
#             list2[i] = 1
#     return list2
# List1 = [1, 2, 3, 4, 5, 1, 3]
# aa= occurance_count(List1)
# print(aa)
#====================================================================================================

# 6.	Write a function return a substring where it starts from 2rd occurrence of ‘a’ and end at 2nd occurrent of ‘b’
# e.g. s = "abracadabra"
# start_char = 'a'
# end_char = 'b'
#
#    Solution:
#
# def find_substring(s, start_char, end_char):
#     # Find the 2nd occurrence of start_char
#     first_index = s.find(start_char)
#     if first_index == -1:
#         return ''  # Not found
#
#     second_index = s.find(start_char, first_index + 1)
#     if second_index == -1:
#         return ''  # Only one occurrence found
#
#     # Find the 2nd occurrence of end_char
#     first_index_b = s.find(end_char)
#     if first_index_b == -1:
#         return ''  # Not found
#
#     second_index_b = s.find(end_char, first_index_b + 1)
#     if second_index_b == -1:
#         return ''  # Only one occurrence found
#
#     # Extract and return the substring
#     return s[second_index:second_index_b + 1]
#
# # Example usage:
# s = "abracadabra"
# start_char = 'a'
# end_char = 'b'
# result = find_substring(s, start_char, end_char)
# print(result)  # Output: "acadab"
#====================================================================================================
# 1. Given a string , write a python code to reverse the string using for loop and slice operator both
# ways?
# Input: city = "ETLQALabs"
# expected output: “sbaL AQ LTE”

# 1.	Using a for loop
# # Input string
# city = "ETLQALabs"

# Reversing using a for loop
# reversed_for_loop = ''
# for char in city:
#     reversed_for_loop = char + reversed_for_loop
#
# print(reversed_for_loop)  # Output: "sbaL AQ LTE"

# 2.	Using the slice operator
# Input string
# city = "ETLQALabs"
#
# # Reversing using slicing
# reversed_slicing = city[::-1]
#
# print(reversed_slicing)  # Output: "sbaL AQ LTE"

# city = "ETLQALabs"
# rev = ""
# for i in city:
#     rev = i + rev #- This places the current character i in front of whatever is already in rev
# print(rev)
#====================================================================================================

# 2. Extract a substring form character "Q" and ends at "b"
# Input: city = "ETLQALabs"
# Expected O/P : QAlab
#
# Code

# Input string
# city = "ETLQALabs"
#
# # Find the starting index of 'Q'
# start_index = city.find("Q")
# # Find the ending index of 'b' (inclusive)
# end_index = city.find("b")
#
# # Extracting the substring
# if start_index != -1 and end_index != -1:
#     substring = city[start_index:end_index + 1]
# else:
#     substring = ''  # Handle cases where 'Q' or 'b' is not found
#
# print(substring)  # Output: "QALab"

#===========================================================================
# city = "ETLQALabs"
# start = city.find("Q")
# end = city.find("b")
# if start != -1 and end != -1:   #- -1 because if the substring is not found.
#     substring = city[start:end+1]
# else:
#     substring = ''
# print(substring)
#====================================================================================================
# 3. Write a python code to check if the given list contains duplicate elements and print yes or no as
# per input
# e.g.
# list1 =[1,2,3,4,3] => Yes
# list2 =[1,2,3,4] => No
# def check_duplicates(input_list):
#     # Convert the list to a set to remove duplicates
#     unique_elements = set(input_list)
#
#     # Compare lengths to check for duplicates
#     if len(unique_elements) < len(input_list):
#         return "Yes"  # There are duplicates
#     else:
#         return "No"  # No duplicates
#
#
# # Example usage
# list1 = [1, 2, 3, 4, 3]
# list2 = [1, 2, 3, 4]
#
# print(check_duplicates(list1))  # Output: Yes
# print(check_duplicates(list2))  # Output: No

#my practice-------------

# def check_duplicate(input_list):
#     list_set = set(input_list)
#     if len(list_set) < len(input_list):
#         return "Yes"
#     else:
#         return "No"
# list1 = [1, 2, 3, 4, 3]
# list2 = [1, 2, 3, 4]
# aa = check_duplicate(list1)
# bb = check_duplicate(list2)
# print(aa)
# print(bb)
#====================================================================================================
# 4. How would you use slicing to create a new list containing only the odd-indexed elements of a
# given list?
# Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output : [1, 3, 5, 7, 9]

# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_list =[]
# for i in l1:
#     if i % 2 == 1:
#         odd_list.append(i)
# print(odd_list)

# def odd_list_values(l1):
#     odd_list = []
#     for i in l1:
#         if i % 2 == 1:
#             odd_list.append(i)
#     return odd_list
# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# aa=odd_list_values(l1)
# print(aa)


# Input list
# input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # Slicing to get odd-indexed elements
# odd_indexed_elements = input_list[1::2]
#
# # Print the result
# print(odd_indexed_elements)  # Output: [1, 3, 5, 7, 9]

#====================================================================================================
# 5. How would you use slicing to create a new list containing only the even-indexed elements of a
# given list?
# Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output : [0, 2, 4, 6, 8]

# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# jj = l1[l1[0]::2]
# print(jj)

# Input list
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing to get even-indexed elements
even_indexed_elements = input_list[0::2]

# Print the result
print(even_indexed_elements)  # Output: [0, 2, 4, 6, 8]
