#Given arry of integers, return a new arry such that each element at index 'i' of the new array is the product of
#all the numbers in the original array except the one at 'i'.
#For example ,if our input was
#[1,2,3,4,5]
#expected output would be
#[120,60,40,30,24]



#by using the library of functools

from functools import reduce
def check(list):
    l=len(list)
    product = reduce(lambda x, y: x * y, list)
    revlist=[]

    for i in range(0,l):

        res=product//list[i]
        revlist+=[res]
    return (revlist)
list=[1,2,3,4,5]
a=check(list)
print(a)



#we can solve this by using NUMPY.PROD also


#by without using any library
def without_lib(list):
    product=1
    res=[]

    for i in list:
        product=product*i       #here we should not write the list[i] because i means the list element only..so it will throw index error
    l=len(list)
    for j in range(0,l):
        pro=product//list[j]
        res+=[pro]
    return res

array=[1,2,3,4,5]
z=without_lib(array)
print(z)



#SUCCESS