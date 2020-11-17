from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a = sorted(intervals, key=lambda x:x[0])
        answer = [a[0]]
        for i in range(1, len(a)):
            if a[i][0] <= answer[-1][-1]:
                answer[-1][-1] = max(a[i][1], answer[-1][-1])
            else:
                answer.append(a[i])
        return answer





if __name__ == '__main__':
    s = Solution()
    ret = s.merge([[1,3],[2,6],[8,10],[15,18]])
    ret = s.merge([[1,4],[2,3]])
    print(ret)

