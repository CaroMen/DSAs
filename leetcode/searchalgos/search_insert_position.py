"""
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order

    INPUTS/OUPUTS
        nums = [1, 3, 5, 6], target = 5 => 2

        nums = [1, 2, 5, 6], target = 2 => 1

    NOTES
        - can probably do a binary search
            - split the list in half
            - find the mid point
            - compare the target to mid point
                - if target is < mid point
                    - set left point to mid point (?)
                - if target is > mid point
                    - set right point to mid point (?)
                - if target == mid point
                    - return index where target is found

        EDGE CASE:
            - if we don't find a match, we have to return the index where the target would be if it were in the list
            -

"""
