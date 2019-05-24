#Given an array of integers, find the first missing positive integer in linear time and  constant space.
#In other words , find the lowest positive integer that does not exists in the arry.The arry can contain
#duplicates and negetive numbers as well.
#For example , the input [3,2,-1,1] should give '2'.
#The input [1,2,0] should give '3'.

def difference_table(list):
    d_list=[]
    for i in list:
        if(i>=0 and i+1>=0):
            dif=abs((i+1)-i)

            d_list.append(dif)
    #print(d_list)
    m=max(d_list)
    for z in d_list:
        for x in range(1,m):
            if(z+x==z+x+1):
                dif=z
    return new_list(dif,list)

def new_list(dif,list):
    val=max(list)+dif
    for i in range(1,val+1):
        a=list.count(i)
        if(a==0 ):
            print(i)
            exit()


list=[1,2,3,34,78,-67]
res=difference_table(list)

#success
#I think there will be some any other method to solve this problem easily....but i too more time for this particular problem










