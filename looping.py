#while loop
#print all 3 digit numbers
# i=100
# while(i<=999):
#     print(i)
#     i+=1
    #for loop
# for i in range(100,1000):
#     print(i)
#colors containing letter b
# colors=['red','green','blue','orange','yellow','black']
# for i in colors:
#     if 'b' in colors:
#         print(i)

#starting with letter g
# for i in colors:
#     if i[0]=='g':
#         print(i)
#all colors except color starting with 'b'
# for i in colors:
#     if i[0]=='b':
#          continue
#     print(i)
#first color starting with 'b'
# for i in colors:
#     if i[0]=='b':
#         print(i)
#     break
#ends with e


# l=[23,45,12,78,90,51,75]
#print all numbers
# for i in l:
#     print(i)

#print all even numbers
# for i in l:
#     if(i%2==0):
#         print(i)

#print those numbers that are divisible by 5
# for i in l:
#     if(i%5==0):
#         print(i)

#stops the loop if i>50
# for i in l:
#     if(i>50):
#         break
#     print(i)

#skip all even numbers
# for i in l:
#     if(i%2==0):
#         continue
#     print(i)

#print the first even number whose value is >50
# for i in l:
#     if(i>50 and i%2==0):
#         print(i)
#         break

#count of all even numbers
# count=0
# for i in l:
#     if(i%2==0):
#         count=count+1
# print("count",count)
#sum of list
# sum=0
# for i in l:
#     sum=sum+i
# print("Sum",sum)

#product of odd number
# product=1
# for i in l:
#     if(i%2!=0):
#         product=product*i
# print("Product",product)

#print each digit in a number
# n=1234
# s=str(n)
# for  i in s:
#     print(i)

#sum of digits in a number
# n=123
# s=str(n)
# sum=0
# for i in s:
#     sum=sum+int(i)
# print(sum)

#product of numbers
# n=12345
# # s=str(n)
# # p=1
# # for i in s:
# #     p=p*int(i)
# # print(p)


#factors of a number
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)

#create a new list with squares of each number
l=[1,2,3,4]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)

#create a new set
# new=set()
# for i in l:
#     new.add(i**2)
# print(new)

# create new dictionary
# l=[1,2,3,4]
# #new={1:1,2:4,3:9,4:16}
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

#reverse of a number
n=1234
s=str(n)
rev=""
for i in s:
    rev=i+rev
print(rev)