def fivo(n):
    if (n <= 1): 
        return n
    else:

        result = 0
        iterA = 0
        iterB = 1

        for i in range(1,n):

            result = iterA + iterB
            iterA = iterB
            iterB = result
        return result

print(fivo(int(input())))