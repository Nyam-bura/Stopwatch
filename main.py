def BinarySearch(list,key):
    low = 0
    high = len(list)-1
    Found = False
#    while low<=high and not Found:
    mid = (low+high)//2
    if key == list[mid]:
        Found = True
        # elif key>list[mid]:
            # low = mid+1
            # else:
                # high = mid - 1
   
if Found = True: 
     print("key is Found") 
else:
    print("key is not Found")       
