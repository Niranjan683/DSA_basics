a=[4,3,9,6,1,2,8]

for i in range (len(a)-1):
    min=i
    for j in range (i+1,len(a)):
        if a[min]>a[j]:
            min=j
    a[i],a[min]=a[min],a[i]
    print(a)
    print()

