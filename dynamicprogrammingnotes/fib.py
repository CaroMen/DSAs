"""
    Write a function fib(n) that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence

    The 1st and 2nd number of the sequence is 1.
    To generate the next nmber of the sequence, we sum the previous two

    INPUT/OUTPUTS
         n: 1, 2, 3, 4, 5, 6, 7,  8,  9, ...
    fib(n): 1, 1, 2, 3, 5, 8, 13, 21, 34, ....
"""


def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))


"""
    DRAWINGS
                            7
                    6                5
                 5      4        4      3
              4    3  3   2    3   2  3   2


        notice the 3 and 2 being repeated. the 2 is our base case so we don't branch out there

"""
