# print if numbers is add or mul or div and soooooonnnnnn
a=int(input("enter number:"))
b=int(input("enter number:"))

user=input("enter which one you want :")
if user=="add":
    print(a+b)
elif user=="sub":
    print(a-b)
elif user=="mul":
    print(a*b)
elif user=="div":
    print(a/b)
elif user=="mod":
    print(a%b)
elif user=="floor":
    print(a//b)
elif user=="square":
    print(a**b)
else:
    print("wrong input")