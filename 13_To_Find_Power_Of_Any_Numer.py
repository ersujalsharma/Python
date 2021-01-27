print("Enter Value of the number")
a=int(input())
print("Enter the value of power")
x=int(input())
prod=1
while(x>0) :
 prod=prod*a
 x=x-1
print("Answer is : "+str(prod))