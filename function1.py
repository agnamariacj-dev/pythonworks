#write a program to find the position of a specific character in a string
# s="hello world"
# ch="l"
# if ch in s:
#     print("The position of", ch ,"is",s.index(ch))
# else:
#     print("Character",ch,"is not present")

#write a program to find the count of a specific character in a string
# s="hello world"
# ch="z"
# if ch in s:
#     print("The count of",ch,"is",s.count(ch))
# else:
#     print("Character ",ch,"is not present")

#write a program to create a new dictionary where keys are letters and values are count of each letter
# s="hello world"
# new={}
# for i in s:
#     if(i.isalpha()):
#         new[i]=s.count(i)
# print(new)

#Write a program to create a new list with 5 random 3 digit numbers
# new=[]
# import random
# for i in range(5):
#     num=random.randint(100,1000)
#     new.append(num)
# print(new)

#write a program to create a 5 digit otp number
# import random
# num=random.randint(10000,100000)
# print(num)
# print("OTP number:",random.randint(10000,100000))

#write a program to find the count of letters,spaces and digits in a string
# s="hello world hello python1234"
# count_l=0
# count_d=0
# count_s=0
# for i in s:
#     if i.isalpha():
#         count_l+=1
#     elif i.isspace():
#         count_s+=1
#     elif i.isdigit():
#         count_d+=1
# print("Letters:",count_l)
# print("Digits:",count_d)
# print("Space:",count_s)

#write a program to create a new dictionary where keys are words and values are length of each word
# s="python coding is easy and fun"
# new={}
# for i in s.split():
#     new[i]=len(i)
# print(new)

#Given a list create a new dictionary where keys are numbers and values are count of each number
# l=[1,1,2,3,4,5,5,5,6,7]
# new={}
# count=0
# for i in l:
#     new[i]=l.count(i)
# print(new)

##
# l=[34,12,56,89,90,11]
#find the largest element
# print("Largest Element:",max(l))

#find the smallest element
# print("Smallest Element:",min(l))

#find the second largest element
# l.sort()
# print("Sorted",l)
# print("Second largest",l[-2])

#find the second smallest element
# l.sort()
# print("Sorted",l)
# print("Second smallest",l[1])
##

##
#Given a dictionary
# d=[["arun",23,40000],
# ["amal",24,50000],
# ["anu",27,30000],
#    ]

#find the maximum salary
# new=[i[2] for i in d]
# print(new)
# print("Maximum salary",max(new))

#find the maximum age
# new=[i[1] for i in d]
# print(new)
# print("Maximum age",max(new))
##

# 1.Given a list
#l=[1,1,1,2,3,3,4,5]
# remove duplicates from list
# new=set()
# for i in l:
#     new.add(i)
# print(new)

# 2.Given a list
#l=[1,1,1,2,3,3,4,5]
# remove duplicates without set()
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

# 3.Given two lists
# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]
# # print common elelments
# s1=set(l1)
# s2=set(l2)
# print("Common elements:",s1.intersection(s2))

# l=[23,56,12,78,98,89,31,67]
# def count_numbers(l):
#     count_even=0
#     count_odd=0
#     count_num=0
#     for i in l:
#         if i%2==0:
#             count_even+=1
#         else:
#                count_odd+=1
#         if i>50:
#             count_num+=1
# print("Even:",count_even)
# print("Odd :",count_odd)
# print("Numbers>50:",count_num)

# l=["red","green","orange","yellow","blue"]
# def length(l):
#     new=[]
#     for i in l:
#         new.append(len(i))
#     return new
# new=length(l)
# print(new)

# def square(n):
#     return n*n
# a=square(5)
# print(a)




