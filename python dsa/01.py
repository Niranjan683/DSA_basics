'''
1)
t=6
h=9
x=0
c=t
if h>t:
    while c<h:
        x=x+c
        c+=1
    print(x)
2)
i=3
while i != 0:
    print(i+3, end='')
    i-=1
'''

'''n=30
s=[]
t=[]
for i in range (2,n+1):
    if n%i==0:
        s.append(i)
if len(s)==7:
    for i in s:
        if i==2:
            t.append(i)
        else:
            for j in range(2,i):
                if i%j!=0:
                    t.append(i)
print(s)
print(t)
c=1
for i in t:
    c=c*i 
if c==n:
    print('yes')
else:
    print('no')'''





 
l=[5,5,5,5,4,5,5,5]
a=l[0:3]
b=l[3:6]
c=l[6:]

if sum(a)==sum(b):
    if c[0]<c[1]:
        print(c[0])
    else:
        print(c[1])

else:
    if sum(a)<sum(b):
        if a[0]==a[1]:
            print(a[2])
        elif a[0]==a[2]:
            print(a[1])
    else:
        if b[0]==b[1]:
            print(b[2])
        elif b[0]==b[2]:
            print(b[1])































