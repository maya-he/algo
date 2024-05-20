def BinRecur(n):
    if n==1:
        return 1
    else:
        return BinRecur(n//2)+1