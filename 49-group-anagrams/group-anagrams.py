class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        tmp = ""
        for word in strs:
            key = ''.join(sorted(word))
            d[key].append(word)
        return list(d.values())