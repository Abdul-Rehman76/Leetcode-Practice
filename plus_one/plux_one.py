class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Here the idea is to convert the list in a string with no spaces that string will be converted to number, that will be added by one and again converted back to string which will be converted back to an integer array and will be returned"""
        my_str="".join(map(str, digits))
        my_num=int(my_str)
        my_num=my_num+1
        my_num = str(my_num)
        new_arr=[]
        for i in my_num:
            new_arr.append(int(i))
        return  new_arr
