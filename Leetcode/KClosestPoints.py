class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        ans = []
        for i in points:
            temp.append((i[0]*i[0] + i[1]*i[1], i))
        temp.sort()
        for i in range(k):
            ans.append(temp[i][1])
        return ans
