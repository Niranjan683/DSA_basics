a=[1,2,3,4,5,6]
T=10
l=0
r=len(a)-1
while l<r:
    if a[l]+a[r] == T:
        print('values : ',a[l],a[r])
        print('indeces :',l,r)
        break
    elif a[l]+a[r] > T:
        r-=1
    else:
        l+=1
        

