def superDigit(n, k):
    if n<10:
        return n
    sum1=0
    while n>0:
        sum1+=n%10
        n//=10
    return superDigit(sum1, k)
