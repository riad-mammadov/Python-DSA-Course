def findTarget(arr,target):
    if len(arr) == 0:
        return False
    if arr[0] == target:
        return True
    else:
        return findTarget(arr[1:], target)
    
print(findTarget([1,2,3,4],9))