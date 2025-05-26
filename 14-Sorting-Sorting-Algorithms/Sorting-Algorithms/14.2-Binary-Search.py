# Notes:
# arr + target - Array must be sorted
# e.g - [10,23,35,45,50,70,85] target = 50
# Steps:
# Start from 0, end = n-1
# See the middle element: end - start // 2 
# // to remove any decimals as index cant be decimal
# Compare element at mid with target ( > || < )
# If mid > target or < target you can half search field accordingly
# 45 < 50 so start will now be at arr[mid+1]
# Second iteration, 70 > 50 so end will move
# repeat steps until target is reached

def binary_search(arr,target):
    size = len(arr)-1
    start = 0
    end = size - 1

    while start <= end:
        mid = end + start // 2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
        
        elif arr[mid] < target:
            start = mid+1


    

arr = [10,23,35,45,50,70,85]
target = 50

print(binary_search(arr,35))
