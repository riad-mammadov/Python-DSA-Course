def helper(l1,x,s,e):
    if (s>e):
        return False
    m = s + (e-s)//2
    
    if (l1[m] == x):
        return True
    
    if (x > l1[m]):
        return helper(l1,x,m+1,e)
    
    return helper(l1,x,s,m-1)


def BinarySearchRec(l1,x):

    return helper(l1,x,0,len(l1)-1)


print(BinarySearchRec([1,2,3,4,5,6,7,8],9))