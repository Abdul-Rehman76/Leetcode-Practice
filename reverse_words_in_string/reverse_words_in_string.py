class Solution:
    def reverseWords(self, s: str) -> str:
        """This reverses the string s but keep the words unreversed by first spliting and then iterarting over the whole array removing any white spaces between string"""
        
        if len(s) < 2:
            return s
        
        s_arr= s.split(" ")
        s_arr_2=[]

        for val in s_arr:
            if val == ' ' or val == '':
                continue
            s_arr_2.append(val)
        return " ".join(s_arr_2[::-1])

