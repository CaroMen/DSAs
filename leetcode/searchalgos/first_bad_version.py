"""
    You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

    INPUT/OUTPUTS
        n = 5, bad = 4 => 4
        explanation:
            call isBadVersion(3) => false
            call isBadVersion(4) => true
            call isBadVersion(5) => true

    TECHNIQUE
        - n is the length of our array. it's the number of versions we have
            - n = 3 => [1, 2, 3]
        - we could split the list in half and check each side
            - we can check each value and see if the bad version is in that side we're on

    QUESTIONS
        - we don't receive a bad version parameter, so how do we determine which is bad or not
            - im assuming, because it returns a boolean, that we need to do something with that to figure out the solution

"""
