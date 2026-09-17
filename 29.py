from math import acos
from math import degrees
s=input()
a,b,c=s.split()
a1=degrees(acos((int(b)**2 + int(c)**2 - int(a)**2)/(int(c)*int(b)*2)))
b1=degrees(acos((int(a)**2 + int(c)**2 - int(b)**2)/(int(c)*int(a)*2)))
c1=degrees(acos((int(b)**2 + int(a)**2 - int(c)**2)/(int(a)*int(b)*2)))
print(round(a1,2),round(b1,2),round(c1,2))
