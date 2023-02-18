class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # initialize a queue for bfs
        queue = []

        # initialize a discovery grid
        discovered = {}
        for i in range(len(grid)):
            discovered[i] = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # find the starting point
                if grid[i][j] == '*':
                    queue.append((i, j, 0))
                    # set start discovered
                    discovered[i].append(True)
                    continue
                discovered[i].append(False)

        # start bfs
        while queue:

            currentI, currentJ, level = queue.pop(0)
            # check four directions
            for i, j in [(currentI-1, currentJ),(currentI+1, currentJ),(currentI, currentJ-1),(currentI, currentJ+1)]:
                # if inside grid boundaries
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    # break if found the food
                    if grid[i][j] == '#':
                        return level + 1
                        
                    # can go from here
                    elif grid[i][j] != 'X':
                        # not discovered
                        if discovered[i][j] == False:
                            discovered[i][j] = True
                            queue.append((i, j, level + 1))

        # if there is no way 
        return -1
