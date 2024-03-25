def caching_fibonacci(n):
    cache ={}
    Debug_Test = False
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            if Debug_Test == True:
                print(f'Easy work: {n}')
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        if Debug_Test == True:
            print(f'Hard work: {n}')
        return cache[n]
        

    return fibonacci(n)
fibo = caching_fibonacci(n=9)
print(fibo)
