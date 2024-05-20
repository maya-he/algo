def euclid(m,n):
    while n != 0:
        r = m % n 
        m = n
        n = r
    return m

print(f"the greatest common factor: {str(euclid(8,4))}")
