import math

x = raw_input("Enter any number")
x = int(x)
n = float(x)
if n > 0:
    digits = int(math.log10(n))+1
elif n == 0:
    digits = 1
else:
    digits = int(math.log10(-n))+2
print digits

#http://stackoverflow.com/questions/2189800/length-of-an-integer-in-python
