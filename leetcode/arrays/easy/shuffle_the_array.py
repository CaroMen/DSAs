# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# INPUTS/OUTPUTS
#   nums = [2, 5, 1, 3, 4, 7], n = 3 => [2, 3, 5, 4, 1, 7]
#   x = [2, 5, 1], y = [3, 4, 7]
#   we want to place each of the y elements right after each of the x elements
#   somewhat like a zip problem
#   create an x_start that starts at the beginning
#   create an x_end that ends at the half point of the list

def shuffle(nums, n):
    res = []

    pointer = n

    for i in range(n):
        res.append(nums[i])
        res.append(nums[pointer])
        pointer += 1

    print(res)
    return res


shuffle([2, 5, 1, 3, 4, 7], 3)
