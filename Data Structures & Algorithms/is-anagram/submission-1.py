class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_map = {}

        for i in s:
            if i in check_map:
                check_map[i] = check_map.get(i, 0) + 1;
            else:
                check_map[i] = 1;
        
        for i in t:
            if i in check_map:
                check_map[i] = check_map.get(i, 0) - 1;
            else:
                check_map[i] = -1;

        for i in check_map.values():
            if not i == 0:
                return False
        
        return True