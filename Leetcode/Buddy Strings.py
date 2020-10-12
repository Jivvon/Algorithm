class Solution:
    # 32ms
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        elif A == B:
            setA = list(set(list(A)))
            if len(setA) < len(A): return True
            else: return False

        x, y = -1, -1
        for i, a in enumerate(A):
            if a != B[i]:
                if x < 0:
                    x = i
                elif y < 0:
                    y = i
                else: return False

        answer = A[:x] + A[y] + A[x+1:y] + A[x] + A[y+1:]
        return answer == B

    # 20ms
    def buddyStrings_20ms(self, A: str, B: str) -> bool:
        if len(A) != len(B) or set(A) != set(B): return False
        if A == B:
            return len(A) - len(set(A)) >= 1
        else:
            indices = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    indices.append(i)
                if counter > 2:
                    return False
            return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]

if __name__ == '__main__':
    s = Solution()
    s.buddyStrings("aa", "aa")
    s.buddyStrings("ab", "ba")
