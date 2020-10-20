import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        current = 0
        dic = {}
        answer = 0
        while(current < len(s)):
            if(s[current] not in dic or max_count > dic[s[current]]):
                answer = max(answer, (current - max_count + 1))
                dic[s[current]] = current
            else:
                max_count = dic[s[current]] + 1
                answer  = max(answer,(current - max_count + 1))
                current -= 1
            current += 1
        return answer
                


s = Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))
