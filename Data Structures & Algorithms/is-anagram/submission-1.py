class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map1={}
        for char1 in s:
            count_map1[char1]=1+count_map1.get(char1,0)
        
        count_map2={}
        for char2 in t:
            count_map2[char2]=1+count_map2.get(char2,0)
        
        if count_map1==count_map2:
            return True
        else:
            return False
