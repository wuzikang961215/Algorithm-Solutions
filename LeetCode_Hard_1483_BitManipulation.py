class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """

        self.n = n
        self.parent = parent
        
        # build a binary lifting list
        self.iparent = collections.defaultdict(list)
        # at most there are 2^17 levels
        for i in range(17):
            # for every power of two level, there are n nodes
            for j in range(len(parent)):
                self.iparent[i].append(-1)

        # get all 2^i parents of each node
        for j in range(len(parent)):
            # first parent of each node
            self.iparent[0][j] = parent[j]

        for level in self.iparent:
            if level == 0:
                continue
            # set ancestor for each level
            # temp is intermediate parent, i.e. 8th parent is 4th parent's 4th parent
            for node in range(len(self.iparent[level])):
                temp = self.iparent[level - 1][node]
                if temp != -1:
                    self.iparent[level][node] = self.iparent[level - 1][temp]


    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """

        # assuming k is at most 2 ^ 17
        for i in range(17):
            if k & (1 << i):
                node = self.iparent[i][node]
                if node == -1:
                    return -1

        return node
        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)