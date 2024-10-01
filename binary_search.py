a=list(map(int,input('enter the values :').split(',')))
target=int(input('enter the target :'))
left=0
right=len(a)-1


while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        print('the target element is ',a[mid])
        print('the index of target element is ', mid)
        break
    if a[mid]<target:
        left=mid+1
    
    else:
        right=mid-1
    print(left, right)
else:
    print('the element is not in the list')