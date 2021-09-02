# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

"""
    INPUTS/OUTPUTS
        nums = [1, 1, 1], k = 2 => 2

    PATTERN
        - we need to keep count of the prefix
        prefix_sums = {0: 1}

        [1, -1, 1, 1, 1, 1], k = 3

        EDGE CASE
            - when we loop through the list, and we get to index 2, our sum is going to be equal to 3
            - so when we do 3 - 3, we get 0
            - we need to set our prefix count to have prefix of 0 and count of 1

        LOOP
            - we start at 1, so we do 1 - 3 = -2
                - does -2 exist in our prefix map? nope so we continue
                - BUT we want to take the prefix we just computed of 1 and add it to our prefix map
                - {0: 1, 1: 1, }
            - we go to -1, so now we have a sum of 0. 0 - 3 = -3
                - is -3 in our prefix map? nope so we can continue
                - we look at the prefix we just computed, 0, and we look to see if it's in our prefix map
                    - it is, so we increment the count
                - {0: 2, 1: 1}
            - we go to 1, so now we have a sum of 1. 1 - 3 = -2
                - is -2 in our prefix map? nope so we continue
                - look at the prefix we just computed, 1, and we look to see if it's in our prefix map
                    - it is, so increment the count
                - {0: 2, 1: 2}
            - we go to the next 1, so now we have a sum of 2. 2 - 3 = -1
                - is -1 in our prefix map? nope so continue
                - look at the prefix we just computed, 2 and we look to see if it's in our prefix map.
                    - it's not, so we add it
                - {0: 2, 1: 2, 2: 1}

"""
