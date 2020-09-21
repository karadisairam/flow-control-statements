n1=int(input("enter 1st number "))
n2=int(input("enter 2nd number :"))
n3=int(input("enter 3rd number :"))
if n1<n2 and n1<n3:
    print("small number is :",n1)
elif n2<n3:
    print("small number is :",n2)
else:
    print("small number is :",n3)