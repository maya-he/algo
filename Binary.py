def F(n):
    if n==0:
        return 1
    else:
        return F(n-1)*n
    
print(F(4))