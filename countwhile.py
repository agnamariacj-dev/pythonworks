#count of those 3 digit numbers that contains digit '3'
# count=0
# i=100
# while(i<=999):
#     s=str(i)
#     if'3' in s:
#         count=count+1
#     i+=1
# print(count)
#count of those numbers that are divisible by 7 or 3 in the range(200-300)
# count=0
# i=200
# while(i<=300):
#     if(i%7==0 or i%3==0):
#         count=count+1
#     i+=1
# print(count)
#count of odd numbers that are divisible by 5 in range(1-100)
# count=0
# i=1
# while(i<=100):
#     if(i%5==0 and i%2!=0):
#         count=count+1
#     i+=1
# print(count)
#count of all palindrome numbers in the range(1-1000)
# count=0
# i=1
# while(i<=1000):
#     if str(i)==str(i)[::-1]:
#         count=count+1
#     i+=1
# print(count)
# #count of number divisible by 3 in the range(1-50)
# count=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         count=count+1
#     i+=1
# print(count)


#sum
#find the sum of first 5 numbers
# s=0
# i=1
# while(i<=5):
#     s+=i
#     i+=1
# print(s)

#sum of those numbers that are divisible by 3 in the range(1-50)
# s=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         s+=i
#     i+=1
# print(s)
#sum of all 3 digit numbers
# s=0
# i=100
# while(i<=999):
#     s+=i
#     i+=1
# print(s)
#sum of first 10 even numbers
# s=0
# i=2
# while(i<=20):
#         s+=i
#         i+=2
# print(s)

#product
#product of series 1,2,3,4,5
# product=1
# i=1
# while(i<=5):
#     product*=i
#     i+=1
# print(product)


#product if first 10 odd numbers(1,3,5,....19)
# product=1
# i=1
# while(i<=19):
#     if(i%2!=0):
#         product*=i
#     i+=1
# print(product)

#product of numbers that contain digit '3' in the range(1-50)
# product=1
# i=1
# while(i<=50):
#     s=str(i)
#     if '3' in s:
#         product*=i
#     i+=1
# print(product)

#factorial of a number entered by user
# n=int(input("enter a number:"))
# fact=1
# i=1
# while(i<=n):
#     fact=fact*i
#     i+=1
# print(fact)
#multiplication table of a number(upto 10)
# n=int(input("Enter number to print table:"))
# i=1
# while(i<=10):
#     print(f"{i}*{n}={i*n}")
#     i+=1

#sum of digits of a number
n=int(input("Enter number:"))
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
print(s)

