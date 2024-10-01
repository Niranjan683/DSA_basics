a=list(map(int,input('enter the values').split()))
b=[i for i in a]

c=0
for i in range(len(a)):
    for j in range(0,len(a)-1):
        if a[j]>a[j+1]:
            c+=1
            a[j],a[j+1]=a[j+1],a[j]
        #print(a)
    #print()
#print(a)
#print(c)

n=0
#print(b)
for i in range(len(b)):
    for j in range(0,len(b)-1):
        if b[j]<b[j+1]:
            n+=1
            #print(n)
            b[j],b[j+1]=b[j+1],b[j]
        #print(a)
    
#print(b)
#print(n)
print(min(c,n))