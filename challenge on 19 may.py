#Given a list of numbers and a number k, return whether any two or numbers from the list add up to k

def check(arr,total):
    return rec(arr,total,len(arr)-1)
def rec(arr,total,i):
    if total==0:
        return 1
    elif total<0:
        return 0
    elif i<0:
        return 0
    elif total<arr[i]:
        return rec(arr,total,i-1)
    else:
        return rec (arr,total-arr[i],i-1)+rec(arr,total,i-1)







arr=[1,2,3,5,6,7,56]
total=3
res=check(arr,total)
print(res)

#SUCCESS

