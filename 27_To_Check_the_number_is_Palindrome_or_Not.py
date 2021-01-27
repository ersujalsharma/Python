print("Enter Any number")
a=int(input())
temp=a
rev=0
while a>0 :
 rem=a%10
 rev=rev*10+rem
 a=a//10
print("Reverse Number is")
print(rev)
if temp is rev:
 print("Number is Palindrome")
else :
 print("Number is not a palindrome")