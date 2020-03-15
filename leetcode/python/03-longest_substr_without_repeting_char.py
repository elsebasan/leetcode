class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0
        current_len = 1
        max_len = 1
        previous_index = 1
        visited = [-1] * 256
        visited[ord(s[0])] = 0 
        
        for i in range(1,len_s):
            previous_index = visited[ord(s[i])]
            if previous_index == -1 or (i - current_len > previous_index):
                current_len += 1
            else:
                if current_len > max_len:
                    max_len = current_len
                current_len = i - previous_index   
            visited[ord(s[i])] = i
            
        if current_len > max_len:
            max_len = current_len
        return max_len  
