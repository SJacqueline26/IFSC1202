intval1 = 7 
intval2 = -3
intval3 = 0

floatval1 = 2.8
floatval2 = -4.6
floatval3 = 5.0

strval1 = "6"
strval2 = "-7.8"
strval3 = "5a"

print (int(intval1))
print (int(intval2))
print (int(intval3)) 
print (int(floatval1))	   # Note that 2.8 becomes 2
print (int(floatval2))	   # Note that -4.6 becomes -4
print (int(floatval3))
print (int(strval1))
#print (int(strval2))		# Note you will get an error here
#print (int(strval3)) 	   # Note you will get an error here

print (float(intval1))
print (float(intval2))
print (float(intval3))
print (float(floatval1))
print (float(floatval2))
print (float(floatval3))
print (float(strval1))
print (float(strval2))
#print (float(strval3))		# Note you will get an error here

print (str(intval1))
print (str(intval2))
print (str(intval3))
print (str(floatval1))
print (str(floatval2))
print (str(floatval3))
print (str(strval1))
print (str(strval2))
print (str(strval3))		   # No error here