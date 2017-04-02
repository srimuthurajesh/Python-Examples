flag=0
num=int(input("enter the number"))
for i in range(2,int(num/2)):
    if(num % i==0):
        print("it is not prime number")
        flag=1
        i=i+1
        break
if(flag==0):
    print("it is prime buddy")

    

    