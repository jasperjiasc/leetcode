import sys
import collections


class Solution:
    def findTheDifference(self, s:str,t:str):
        d = collections.Counter(s)
        p = collections.Counter(t)
        for i in p.keys():
            if p[i] > d[i]:
                return i
        return ""


if __name__ == "__main__":
    #print(sys.version)
    sol = Solution()
    sol.findTheDifference("abcd", "abcde")

