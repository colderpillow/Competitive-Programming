class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        first = 0
        last = len(height)-1

        while(first<last):
            distance = last - first
            if min(height[first],height[last]) * distance  > area:
                area = min(height[first],height[last]) * distance
            if height[first] <= height[last]:
                first += 1
            else:
                last -= 1
        return area

            
