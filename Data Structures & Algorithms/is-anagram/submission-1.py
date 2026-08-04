class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs={}
        hasht={}
        for i in s:
            if i in hashs:
                hashs[i]=hashs[i]+1
            else:
                hashs[i]=1

        for j in t:
            if j in hasht:
                hasht[j]=hasht[j]+1
            else:
                hasht[j]=1
        return hashs==hasht
        