# while b:        
#   (a,b) = (b,a%b)
# a will be the answer
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
print(gcd(4,6))
