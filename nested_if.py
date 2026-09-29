# num=int(input("Enter a number:"))
# if(num>0):
#     print("Positive")
#     if (num%2==0):
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("Negative")
#     if(num%2!=0):
#         print("Odd")
#     else:
#         primt("Even")

#check whether a number is divisible by 2 and 3
#divisible by 2 and not by 3
#divisible by 3 and not by 2
# not divisible by 2 and 3

num=int(input("Enter the number:"))
if(num%2==0):
    print("Divisible by 2")
    if(num%3==0):
        print("Divisible by 3")
    else:
        print("Not divisible by 3")
else:
    print("Not divisible by 2")
    if (num % 3 == 0):
        print("Divisible by 3")
    else:
        print("Not divisible by 3")