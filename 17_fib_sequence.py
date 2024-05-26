def fibo(n):
    fib_sequence = [0,1]
    for i in range(2,n):
        next = fib_sequence[-1]+fib_sequence[-2]
        fib_sequence.append(next)
    print(fib_sequence)
fibo(10)
