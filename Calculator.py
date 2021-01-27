#calculator
print("Enter Two Numbers")
a=int(input())
b=int(input())
print("Press 1.For Addition")
print("Press 2.For Substraction")
print("Press 3.For Multiplication")
print("Press 4.For Division")
c=int(input())
def switch(c) :
 switcher = {
	 1: print(a+b),
	 3: print(a*b),
	 4: print(a/b) 
         }
         func = switcher.get(c, lambda: "Invalid month")
         print func()	 