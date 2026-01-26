import time
count=0
t=time
start_time=time.time()
def complexRec(n, c):
    c += 1
    if n <= 2:
        return c

    p = n
    while p > 0:
        temp = [0] * n
        for i in range(n):

            temp[i] = i ^ p
        p >>= 1

    small = [0] * n
    for i in range(n):

        small[i] = i * i

    if n % 3 == 0:
        small.reverse()
    else:
        small.reverse()

    c=complexRec(n // 2, c)
    complexRec(n // 2, c)
    complexRec(n // 2, c)
    return c
end_time=time.time()
print(f"{complexRec(130, count)}, {(end_time-start_time)*1000: .3f}")

# Recurrence Relation = 3T(n//2) + nlog(n) + n
# Time Complexity= n^(log(3))
# somehow execution time = 0.000 ms
# depth= log(n)-1 (-1 because it stops at <=2 not <=1) (7 for this input)
