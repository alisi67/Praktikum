i=int(input())
h=i//3600
m=(i-h*3600)//60
s=(i-h*3600-m*60)
print(h,':', m,':', s)

