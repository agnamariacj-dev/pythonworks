# n=int(input("Enter number to print table:"))
# i=1
# while(i<=10):
#     print(f"{i}*{n}={i*n}")
#     i+=1

# d={'a':10,'b':20,'c':80}
# for i in d:
#     print(i,d[i])

# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print(i)

l=[['lion','tiger'],['cat','elephant']]
for i in l:
    print("outer loop iteration",i)
    for j in i:
        print(j,end=" ")
    print(j)



