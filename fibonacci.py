class Find_fibonacci:
    def find_fibonacci(self, n):
        fib_1 = 1
        fib_2 = 1        
        i = 0

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        while i < n - 2:
            fib_sum = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_sum
            i = i + 1
        return fib_sum