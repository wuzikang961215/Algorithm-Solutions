class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """

        output = [0] * len(puzzles)

        wordset = {}

        # transfer words to sets
        for word in words:
            if frozenset(word) not in wordset:
                wordset[frozenset(word)] = 0
            wordset[frozenset(word)] += 1

        # map to record indexes that contains each char
        charmap = collections.defaultdict(set)

        # iterate through words first
        for word in wordset:
            indexes = set(range(len(puzzles)))
            # check each char
            for char in list(word):
                # only iterate puzzles array when char not in map yet
                if char not in charmap:
                    for i, puzzle in enumerate(puzzles):
                        if char in puzzle:
                            # add index to corresponding char
                            charmap[char].add(i)
                # get intersections of indexes of all characters
                indexes &= charmap[char]
            
            # for every index left, add 1 appearance
            for index in list(indexes):
                if puzzles[index][0] in word:
                    output[index] += wordset[word]     

        return output