class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """This find the ranges in given array"""
        range_arr=[]
        if len(nums)==0:
            return range_arr
        if len(nums) == 1:
            range_arr.append(str(nums[-1]))
            return range_arr
        start=nums[0]
        steps=0
        for i in range(1,len(nums)):
            steps=steps+1
            if abs(nums[i]-start) == steps and i==(len(nums)-1):
                range_arr.append(str(start)+"->"+str(nums[i]))
            if abs(nums[i]-start) == steps:
                continue
            
            else:
                if nums[i-1]==start:
                    range_arr.append(str(start))
                else:
                    range_arr.append(str(start)+"->"+str(nums[i-1]))
                start=nums[i]
                steps=0
                if start == nums[-1]:
                    range_arr.append(str(start))
                    

        return range_arr
