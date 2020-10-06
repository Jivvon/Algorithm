# 12ms
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        if N == 1: return 0
        up = 2
        while up <= N:
            up = up << 1

        return up -1 -N


# 28ms
# class Solution:
#     def bitwiseComplement(self, N: int) -> int:
#         if N == 0: return 1
#         s = 0
#         place_value = 1
#         while N > 0:
#             s += (1^N%2) * place_value
#             place_value *= 2
#             N //= 2
#         return s

# 내 코드 (28ms)
# class Solution:
#     def bitwiseComplement(self, N: int) -> int:
#         b = list(bin(N)[2:])
#         ll = list(map(lambda x: abs(int(x)-1) , b))
#         po, answer = 0,0
#         while ll:
#             n = ll.pop()
#             answer += n * pow(2, po)
#             po += 1
#
#         return answer



if __name__ == '__main__':
    s = Solution()
    s.bitwiseComplement(4)
    s.bitwiseComplement(5)
    s.bitwiseComplement(6)
    s.bitwiseComplement(7)
    s.bitwiseComplement(8)
    s.bitwiseComplement(10)
