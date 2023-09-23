arr=[]
#input an array with a size
size=int(input("enter size of array"))
for i in range(0,size):
               element=int(input("enter element"))
               arr.append(element)
n=len(arr)

#for every pass a for loop
for j in range(1,n):
    key=arr[j]
    i=j-1
    while i>=0 and arr[i]>key:
        #move element to the right
        arr[i+1]=arr[i]
        i=i-1
    #to insert key at correct position
    arr[i+1]=key
print(arr)
