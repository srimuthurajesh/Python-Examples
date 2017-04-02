from random import randrange
print("Welcome to guessing game, Rock it")
n=randrange(1,10)     #n=random.randomrange(1,10)
points=0
  
while(1<2):
    num = int(input("guess the number between 1 to 10:  "))
    if(num<n):
        print("Answer is higher")
        points=points+1
    elif(num>n):
        print("Answer is lower")
        points=points+1
    elif(num==n):
        print("The answer is correct, U nailed it . Keep it up")
        break

print("You took "+str(points)+" chances to guess")
    