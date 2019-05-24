def difference(list):
    for i in list:
        if (i>0 and i+1>0):
            if(abs((i+1)-i)==abs((i+2)-(i+1))):
                dif=abs((i+1)-i)
                break
    return new_list(dif,list)


def new_list(dif,list):
    val=max(list)+dif
    for j in range(1,val+1):
        c=list.count(j)
        if c==0 and abs(j-list[0])==dif:
            res=j
            break




    print(res)



list=[1,2,0]
difference(list)

#FAIL