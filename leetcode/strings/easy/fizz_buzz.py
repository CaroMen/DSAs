# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.

"""
    INPUTS/OUTPUTS
        n = 3 => ["1", "2", "Fizz]
        n = 5 => ["1", "2", "Fizz", "4", "Buzz]

    NOTES

"""


def fizzBuzz(n):
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 5 == 0:
            res.append("Buzz")
        elif i % 3 == 0:
            res.append("Fizz")
        else:
            res.append(str(i))
        # print(str(i))

    # pass
    print(res)
    return res


fizzBuzz(15)
