arr=[123,456,132,435,355]
print(arr)
input=input("What is your number?")
def linearsearch(arr,input):
    for i in range(len(arr)):
        if arr[i]==input:
            return i
        return -1
print("I found the number is position",linearsearch(arr,input))

print()
print("binarysearch")
def binarySearch(arr1,start,end,x):
    if end>=start:
        mid=start+(end-start)//2
        if arr1[mid]==x:
            return mid
        elif arr1[mid]>x:
            return binarySearch(arr1,start,mid-1,x)
        else:
            return binarySearch(arr1,mid+1,end,x)
    else:
        return -1
arr1=sorted(["a","b","c","d"])
x=input("What is your number?")
result=binarySearch(arr1,0,len(arr1)-1,x)
if result!=-1:
    print("Element is present"+str(result))
else:
    print("Element is not present")