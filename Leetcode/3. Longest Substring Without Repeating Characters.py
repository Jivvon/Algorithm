class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strs = map(ord, s)
        ret = 0
        answer = []
        for ch in strs:
            if ch not in answer:
                answer.append(ch)
            else:
                ret = max(ret, len(answer))
                answer = answer[answer.index(ch)+1:]
                answer.append(ch)

        ret = max(ret, len(answer))
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("dvdf"))
