def Merge(l1,s,m,e):
    l, r = s, m + 1
    ans = []
    while l <= m and r <= e:
        if l1[l] < l1[r]:
           ans.append(l1[l])
           l += 1
        elif l1[r] < l1[l]:
            ans.append(l1[r])
            r += 1
        elif l1[l] == l1[r]:
            ans.append(l1[l])
            ans.append(l1[r])
            l += 1
            r += 1
    while (l<=m):
        ans.append(l1[l])
        l += 1
    while (r<=e):
        ans.append(l1[r])
        r+=1
    
    startAns = 0
    startOfList = s

    while startOfList <= e:
        l1[startOfList] = ans[startAns]
        startAns += 1
        startOfList += 1

    return

def MergeSortHelper(l1,s,e):
    if s>=e:
        return
    m = s + (e-s)//2

    MergeSortHelper(l1,s,m)
    MergeSortHelper(l1,m+1,e)

    Merge(l1,s,m,e)


def MergeSort(l1):
    return MergeSortHelper(l1,0,len(l1)-1)

# 1,6,9,1 | ,2,4,4
l1 = [1,9,6,4,2,4,1]
MergeSort(l1)
print(l1)