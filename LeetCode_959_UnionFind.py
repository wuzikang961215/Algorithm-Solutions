class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        n = len(grid)
        self.parents = range(4*n*n) # for finding
        
        def find(a):
            if self.parents[a] == a:
                return a
            return find(self.parents[a])

        def union(a, b):
            self.parents[find(b)] = find(a)

        # traverse through each cell of grid
        for i, line in enumerate(grid):
            for j, char in enumerate(line):
                north = 4*i*n + 4*j # north
                west = 4*i*n + 4*j + 1 # west
                east = 4*i*n + 4*j + 2 # east
                south = 4*i*n + 4*j + 3 # south
                if char == '/': # union left part
                    union(north, west)
                    union(east, south)
                elif char == '\\':
                    union(north, east)
                    union(west, south)
                elif char == ' ':
                    union(north, west)
                    union(east, south)
                    union(north, east)

                # unite south and north neighbors
                if i+1 < len(grid):
                    union(south, south + 4 * n - 3)
                if i-1 >= 0:
                    union(north, north - 4 * n + 3)
                # unite east and west neighbors
                if j+1 < len(grid):
                    union(east, east + 3)
                if j-1 >= 0:
                    union(west, west - 3)
            
        # check how many components
        regions = 0
        for i, parent in enumerate(self.parents):
            if i == parent:
                regions += 1

        return regions