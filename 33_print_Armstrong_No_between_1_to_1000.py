for a in range(1,1000) : 
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
  print(temp ,end=" ")