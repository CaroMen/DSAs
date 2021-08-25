# Count the number of prime numbers less than a non-negative number, n.

"""
    INPUTS/OUTPUTS
        n = 10 => 4

    NOTES
        prime is a num that's only divisible by itself or 1
        loop through range of n
        if i % 1 == 0 or i % i == 0:
            counter += 1

"""


def primeNums(nums):
    # if nums <= 2:
    #     return 0

    # primes = [1] * nums

    # idx = 2

    # while idx < nums:
    #     temp = idx
    #     if primes[idx]:
    #         temp += idx
    #         while temp < nums:
    #             primes[temp] = 0
    #             temp += idx
    #     idx += 1

    # return sum(primes) - 2
    count = 0

    for idx in range(2, nums):
        num = nums[idx]

        if isPrime(idx):
            count += 1

    return count


def isPrime(num):
    sqrt = math.floor(math.sqrt(num))

    for idx in range(2, sqrt):
        if num % idx == 0:
            return False
    return True


primeNums(10)
