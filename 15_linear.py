def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print("Element present in ", i, " index")
            return

    print("Element not present")

arr = [2, 3, 6, 19, 6, 87]
linear_search(arr, 546)
