def duplicate(arr):
    ans = []
    for i in arr:
        if i not in ans:
            ans.append(i)

    return ans
arr = [1,2,2,2,3,3,4,4,4,4,4,5,5,5,5]
print(duplicate(arr))
