pre,cur=0,1
print("Enter no Of Terms")
a=int(input())
print("Prime Numbers Are:")
for i in range(0,a):
 new=pre+cur
 print(pre, end=" ")
 pre=cur
 cur=new



