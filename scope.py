#Global
# x=20 #global
# print("outside",x)
#
# def f():
#     print("inside",x)
# f()
#Local
# def f():
#     x=20#local
#     print("inside",x)
# f()
#
# print("outside",x)

#enclosing/nonlocal
def outer():
    x=20
    def inner():

        print("inside inner function",x)
    inner()
    print("inside outer function",x)
outer()