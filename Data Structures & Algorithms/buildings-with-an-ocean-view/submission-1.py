class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        maxheight = heights[-1]
        highbuildings = [n-1]
        for i in range(n-2, -1, -1):
            if heights[i] > maxheight:
                maxheight = heights[i]
                highbuildings.append(i)
        return list(reversed(highbuildings))