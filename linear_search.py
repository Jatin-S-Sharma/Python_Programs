arr=[23,45,67,12,94,34,62,38,59,46]
loc=1
item=622
#insert elemment at last
arr.append(item)
n=len(arr)

#traverse array until you get the item
while(arr[loc]!=item):
    loc=loc+1
loc+=1
# if item found at nth position or at last
if loc==n:
    loc=0
    print("not fouund")
else:
    print("found at",loc)
