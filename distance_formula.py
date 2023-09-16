def input_coordinate():
    x1=int(input("enter X1"))
    y1=int(input("enter y1"))
    x2=int(input("enter X2"))
    y2=int(input("enter y2"))
    data=   (x2-x1)**2+(y2-y1)**2
    return data**0.5

    
    
def print_distance():
    print(input_coordinate())
print_distance()
    
    


