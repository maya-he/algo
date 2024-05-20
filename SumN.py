s = 0
k = -1
a=[1,2,3,4,5]

def SumN (N):
    s = 0
    k= -1 
    while (k < N-1):
        k += 1
        s += a[k]
    return s

print(SumN(len(a)))