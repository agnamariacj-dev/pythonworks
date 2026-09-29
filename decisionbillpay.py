#write a program to calculate the electricity bill based on the following
# units=int(input("Enter units"))
# if units<=100:
#     bill=0
# elif units>100 and units<=200:
#     bill=0+(units-100)*5
# elif units>200 and units<=300:
#     bill=0+500+(units-200)*10
# else:
#     bill=0+500+1000+(units-300)*15
# print("Bill is",bill)

#write a program to check whetrher the
# num=int(input("Enter the number:"))
# if(num>9 and num<=99):
#     print("2 digit number")
# elif(num>99 and num<=999):
#     print("3 digit number")
# else:
#     print("4 digit number")


#write a basic calculator program(+,_,*,/,%,//)
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# opr=input("Enter operatoion:")
# if(opr=='+'):
#     print("sum is:",(num1+num2))
# elif(opr=='-'):
#     print("difference is:", (num1 - num2))
# elif(opr=='*'):
#     print("product is:", (num1 * num2))
# elif (opr == '/'):
#     print("result is:", (num1 / num2))
# elif(opr=='%'):
#     print("modulus is:", (num1 % num2))
# else:
#     print("floor division is:", (num1 // num2))

#write a program to print the number
l1=['January','March','May','July','August','October','December']
l2=['April','June','September','November']
l3=['February']
month=input("Enter month:")
if month in l1:
    print(f"{month} has 31 days")
elif month in l2:
    print(f"{month} has 30 days")
else:
    print(f"{month} has 28 or 29 days")