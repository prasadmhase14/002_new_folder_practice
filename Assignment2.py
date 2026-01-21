#1.	Write a function to return a list with all the duplicate elements from the list

# def findDuplicateElements(inputList):
#     # initiate an empty dictionary to count the occurrence of each elements
#     # initiate an empty list to store all the duplicate elements only and return to the function
#     dictionaryForElementsCounts = {}
#     listOfDuplicateElements = []
#
#     # Iterate through the input list and store the occurrences of each element in dictionary
#     for element in inputList:
#         if element in dictionaryForElementsCounts:
#             dictionaryForElementsCounts[element] += 1
#         else:
#             dictionaryForElementsCounts[element] = 1
#
#     # Add all the duplicate elements in the list ( which are having counts > 1 )
#     for element, count in dictionaryForElementsCounts.items():
#         if count > 1:
#             listOfDuplicateElements.append(element)
#
#     return listOfDuplicateElements
#
#     # Calling and execute the function
# inputList =[1, 2, 3, 1, 7, 3,4, 2, 5, 6,]
# ansList = findDuplicateElements(inputList)
# print(ansList)

# def duplicate_list():
#     l1 =[11,11,22,22,33,33,55,55,555,555,77,88,3,4]
#     duplicate=[]
#     for i in range (len(l1)):
#         for j in range(i+1,len(l1)):
#             if l1[i]== l1[j]:
#                 duplicate.append(l1[i])
#     return duplicate
# aa=duplicate_list()
# print(aa)

# def duplicate_list(l1):
#     duplicate=[]
#     for i in range (len(l1)):
#         for j in range(i+1,len(l1)):
#             if l1[i]== l1[j]:
#                 duplicate.append(l1[i])
#     return duplicate
# l1 =[11,11,22,22,33,33,55,55,555,555,77,88,3,4]
# aa=duplicate_list(l1)
# print(aa)

#2.	Write a function to return a list with all the singly occurred elements ( which appear only once ) from the list

# def findSinglyOccurredElements(inputList):
#     # initiate an empty dictionary to count the occurrence of each elements
#     # initiate an empty list to store all the duplicate elements only and return to the function
#     dictionaryForElementsCounts = {}
#     listOfSinglyOccuredElements = []
#
#     # Iterate through the input list and store the occurrences of each element in dictionary
#     for element in inputList:
#         if element in dictionaryForElementsCounts:
#             dictionaryForElementsCounts[element] += 1
#         else:
#             dictionaryForElementsCounts[element] = 1
#
#     # Add all the duplicate elements in the list ( which are having counts > 1 )
#     for element, count in dictionaryForElementsCounts.items():
#         if count == 1:
#             listOfSinglyOccuredElements.append(element)
#
#     return listOfSinglyOccuredElements
#
# # Calling and execute the function
# inputList =[1, 2, 3, 1, 7, 3,4, 2, 5, 6,]
# ansList = findSinglyOccurredElements (inputList)
# print(ansList)


# l1=[11,11,22,22,3,4,5]
# unique=[]
# for i in l1:
#     if l1.count(i)==1:
#         unique.append(i)
# print(unique)

# def unique_list():
#     l1=[11,11,22,22,3,4,5]
#     unique=[]
#     for i in l1:
#         if l1.count(i)==1:
#             unique.append(i)
#     return unique
# #print(unique_list())
# aa = unique_list()
# print(aa)

#3.	Write a Python program to find the sum of all elements in the list and print.


# l1=[1,2,3]
#     sum=0
#     for i in l1:
#         sum = sum + i
#     print(sum)

# def sum_of_list():
#     l1=[1,2,3]
#     sum=0
#     for i in l1:
#         sum = sum + i
#     return sum
# aa=sum_of_list()
# print(aa)

# def sum_of_list(l1):
#     sum=0
#     for i in l1:
#         sum = sum + i
#     return sum
#
# l1=[1,2,3]
# print(sum_of_list(l1))


#4.	Write a program to find the largest number in the list and return.
# def printTheBiggestNumber(inputList):
#     biggestNumber = inputList[0]
#     # Iterate through the list and compare find the biggest number
#     for element in inputList:
#         if biggestNumber < element:
#             biggestNumber = element
#     print("The biggest number from the given list is :",biggestNumber)
# # Calling and execute the function
# inputList =[1,2,9,3,4,5]
# printTheBiggestNumber (inputList)

#basic approach
# l1=[1,2,3,4]
# largest =max(l1)
# print(largest)

#Manula approach
# l1=[1,2,3,4]
# largest= l1[0]   #suppose we assume this is the largest
# for i in l1:
#     if i > largest:
#         largest = i
# print(largest)

# def max_number(l1):
#     largest= l1[0]   #suppose we assume this is the largest
#     for i in l1:
#         if i > largest:
#             largest = i
#     return largest
#
# l1=[1,2,3,4]
# aa=max_number(l1)
# print(aa)

#5.	Remove Duplicates from a List and return the list

#set because set dont have duplicate values
# def removeDuplicates(inputList):
#     return set(inputList)
# inputList =[1,2,9,3,4,5,1,2,3]
# print(removeDuplicates (inputList))


#for loop
# l1 = [11, 11, 22, 22, 3, 4, 5]
# unique_list = []
# for item in l1:
#     if item not in unique_list:
#         unique_list.append(item)
# print(unique_list)

#in function
# def unique_in_list():
#     l1 = [11, 11, 22, 22, 3, 4, 5]
#     unique_list = []
#     for item in l1:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list
# aa=unique_in_list()
# print(aa)

#6.	Find the Second Largest Element and print.
def secondLargestNumber(inputList):
    inputList.sort()
    print("After Sorting the list : ",inputList)
    return inputList[-2]

inputList =[1,2,9,3,4,5,7,1,2,3]
print(secondLargestNumber (inputList))

# l1 = [11, 22, 3, 45, 7, 99, 4]
# # Remove duplicates, sort in descending order
# sorted_list = sorted(set(l1), reverse=True)
# second_largest = sorted_list[1]
# print(second_largest)

# l1 = [11, 22, 22, 3,3,3, 45, 7, 99, 4]
# sorted_list = sorted(set(l1))
# reverse_sorted_list = list(reversed(sorted_list))
# print(reverse_sorted_list)
# print("2nd largest number :",reverse_sorted_list[1])

