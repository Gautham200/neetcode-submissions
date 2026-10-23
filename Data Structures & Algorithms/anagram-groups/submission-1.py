class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j)-ord('a')] += 1
            d[tuple(count)].append(i)
        res = []
        for i in d:
            res.append(d[i])
        return res