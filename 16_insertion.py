def insertion(arr):
    n = len(arr)
    for i in range(0,n):
        j = i
        while(j>0):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    
    return arr

arr = [58,56,31,20,18,17,6]
print(insertion(arr))
