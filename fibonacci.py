def fib_dan(n):
    if n <= 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(n-2):
            c = a + b
            a = b
            b = c

        return c
    
    '''
    if n < 2:
        return n
    return fib_dan(n-2) + fib_dan(n-1)
    '''
    
print(fib_dan(6))
