a=list(map(int,input('enter the values : ').split(',')))
target=int(input("Enter Your Target : "))
for i in range(len(a)):
    if a[i]!=target:
        continue
    else:
        print('the index of {} is {}'.format({target},{i}))
    

