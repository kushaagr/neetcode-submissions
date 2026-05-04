class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        next_greater_index = [-1] * n
        monostack = []
        for i in range(n):
            while monostack and heights[i] >= heights[monostack[-1]]:
                top = monostack.pop()
                next_greater_index[top] = i
            monostack.append(i)
        return sorted(i for i in range(n) if next_greater_index[i] == -1)