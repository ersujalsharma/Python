print("Enter Number You Want two Display")
a=int(input())
def One() :
 return 1
def Two() :
 return 2
def three() :
 return 3
def numbers_of_switch(a) :
 switcher = {
	1: One,
	2: Two,
	3: Three
	
	}
func = switcher.get(a)
print func()