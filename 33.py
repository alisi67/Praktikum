s=input()
n,c,y=s.split()
n,c,y=int(n),int(c),int(y)
stro=0
stolb=1
pag=y//(n*c)
k=pag*n*c
z=1
while z!=0:
    k+=1
    if stro<n:
        stro+=1
    if stro==n and stolb<c:
        stro=0
        stolb+=1
    if k==y:
        print(pag,stolb,stro)
        z=0
        
