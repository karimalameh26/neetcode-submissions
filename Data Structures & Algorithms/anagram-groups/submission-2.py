class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for word in strs:
            counter={}
            for i in word:
                if i in counter:
                    counter[i]+=1
                else:
                    counter[i]=1
            key=tuple(sorted(counter.items()))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key]=[word]
        return list(groups.values())
            
            
            


        