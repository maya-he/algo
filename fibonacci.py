def fib_recursion(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)



A = [0,1]

def fib_arr(n):
    for i in range(2,n + 1):
        A.append(A[i-1] + A[i-2])
    return A[n]

print(fib_recursion(9))
print(fib_arr(7))

