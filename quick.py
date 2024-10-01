def quick(a):
    if len(a)<=1:
        return a
    pivot=a[0]  
    left=[i for i in a if i<pivot]
    right=[i for i in a if i>pivot]
    middle=[i for  i in a if i==pivot]

    return quick(left)+middle+quick(right)





a=[4,5,17,6,1,2,8]
print(quick(a))