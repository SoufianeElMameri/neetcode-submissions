class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}

        for itm in strs:
            key = "".join(sorted(itm))
            if key in counts:
                counts[key].append(itm)
            else:
                counts[key] = [itm]
        return list(counts.values())