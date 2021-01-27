#unit conversion/kmto m feet inch and cm	
print("Enter Distance in km")
km=int(input())
print("Your distance is = "+str(km))
m=km*1000
print("Distance in meter = "+str(m))
f=float(3.3*m)
print("Distance in feet = "+str(f))
i=float(f*12)
print("Distance in inch = "+str(i))
cm=float(i*2.54)
print("Distance in cm = "+str(cm))