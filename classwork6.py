# # # Q1.Define a function that takes 2 numbers and returns their product
# def product(a,b):
#     p=a*b
#     return p
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# result=product(a,b)
# print("Product",result)

# # Q2.Define a function that takes a string and returns number of vowels
# def vowels(s):
#     count=0
#     for i in s:
#         if i in "aeiouAEIOU":
#             count=count+1
#     return count
# s=input("Enter a string:")
# print("Number of vowels:",vowels(s))


# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
# def area(l,b):
#     area=l*b
#     return area
# l=int(input("Enter length:"))
# b=int(input("Enter breadth:"))
# result=area(l,b)
# print("Area",result)

# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
# def even(l):
#   a=[]
#   for i in l:
#       if i%2==0:
#           a.append(i)
#   return a
# a=even(l)
# print(a)


# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# def sum(l):
#     a=[]
#     for i in l:
#         s = str(i)
#         sum=int(s[0])+int(s[1])+int(s[2])
#         a.append(sum)
#     return a
# a=sum(l)
# print(a)

#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]
# def list(l):
#     a=[]
#     for i in l:
#        if i not in a:
#            a.append(i)
#     return a
# a=list(l)
# print(a)


#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# def lists(list1,list2):
#     a=[]
#     for i in list1:
#         if i in list2:
#             a.append(i)
#     return a
# a=lists(list1,list2)
# print(a)
