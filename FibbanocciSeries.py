num=int(input("Enter the number of fibbonoci series needed"))
a=0
b=1
print(a)
print(b)
for i in range(0,num-2):
    c=a+b
    print(c)
    a=b
    b=c