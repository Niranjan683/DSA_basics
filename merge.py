def merge(a):
    if len(a)>1:
        mid=len(a)//2
        left= a[0 : mid ]
        right = a[mid:]
        merge(left)
        merge(right)
        lp=0
        rp=0
        fp=0

        while (lp < len(left) and rp < len(right)) :
            if left[lp] < right[rp]:
                a[fp]=left[lp]
                lp+=1
                
            else:
                a[fp]=right[rp]
                rp+=1
            fp+=1

        while lp<len(left):
            a[fp]=left[lp]
            fp+=1
            lp+=1
            
        while rp < len(right):
            a[fp]=right[rp]
            fp+=1
            rp+=1


a=[4,5,17,6,1,2,8]
merge(a)
print(a)