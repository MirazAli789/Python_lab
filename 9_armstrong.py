def dig(n):
    count = 0
    while n != 0:
        n //= 10  # integer division
        count += 1

    return count


def isarm(n):
    org = n
    cnt = dig(n)
    ans = 0
    rem=0
    while n!=0:
        rem = n % 10
        ans += rem**cnt
        n //= 10

    return org == ans

print(isarm(153))

def arm_range(n):
    for i in range(1,n+1):
        if(isarm(i)):
            print(i,end=" ")

arm_range(1000)
