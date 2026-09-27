class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        
        for word in strs:
            key = ''.join(sorted(word))
            if key not in str_dict:
                str_dict[key] = []
            str_dict[key].append(word)

        return [value for key, value in str_dict.items()]
        


        