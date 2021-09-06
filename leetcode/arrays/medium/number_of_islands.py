# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""
    INPUTS/OUTPUTS:
        grid = [
                    ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]
                ]

    NOTES
        - a single "1" surrounded by "0"s will be an island
        - we have to check all the way around our current location
            - so if we have a one at grid[1][1]
            - we need to check grid[0][1], so row - 1
            - also need to check grid[1][0], so col - 1
            - also need to check grid[1][2], so col + 1
            - and also check grid[2][1], so row + 1
        - return how many islands there are
"""


def numIslands(grid):
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                count += 1
