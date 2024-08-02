a=[4,5,17,6,1,2,8]
'''for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        for j in range(0,i+1):
            if a[i+1]<a[j]:
                a[i+1],a[j]=a[j],a[i+1]
        print(a)
        print()
'''

for i in range (1,len(a)):
    cur=a[i]
    j=i-1
    while j>=0 and cur<a[j]:
        a[j+1]=a[j]
        j-=1 
    a[j+1]=cur

    print(a)
    print()
    
