# Say that you are a traveler on a 2D grid. You begin in the top left corner and your goal is to travel to the bottom right corner. You may only move down or right

# In how many ways can you travel to the goal on a grid with dimensions m * n?

def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


# print(grid_traveler(1, 1))  # 1
# print(grid_traveler(2, 3))  # 3
# print(grid_traveler(3, 2))  # 3
# print(grid_traveler(3, 3))  # 6
# print(grid_traveler(18, 18))  # 2333606220

def optimized_grid_travel(m, n, memo={}):
    key = str(m) + ', ' + str(n)

    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    memo[key] = optimized_grid_travel(
        m - 1, n, memo) + optimized_grid_travel(m, n - 1, memo)

    return memo[key]


print(optimized_grid_travel(18, 18))
print(optimized_grid_travel(1, 1))
print(optimized_grid_travel(3, 2))
