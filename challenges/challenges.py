def caesar(lst):
    totalSum = 0
    product = 0
    for nums in lst:
        totalSum += nums
        product *= nums

    
    return product % totalSum == 0
      
print(caesar([2,3,4,5,6]))