def factorial_dan(n):
    c = 1
    for i in range(1, n + 1):
        c = c * i
        
    return c
    '''
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    '''
    
print(factorial_dan(4))
