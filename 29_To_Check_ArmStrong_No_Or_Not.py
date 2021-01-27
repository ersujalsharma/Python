print("enter any number")
a=int(input())
temp=a
count=0
while a>0 :
 count=count+1
 a=a//10
arm=0
a=temp
while a>0 :
 rem=a%10
 arm=arm+rem**count
 a=a//10
if temp == arm :
 print("No is Armstrong")
else :
 print("Not a ArmStrong no")