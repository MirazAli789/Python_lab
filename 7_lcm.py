def least_common(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            break

        max_num += 1

    return max_num


print(least_common(5, 25))
arr = [123,2,4,634]

if(123 not in arr):
    print("Not present in arr")

else:
    print("present in arr")



