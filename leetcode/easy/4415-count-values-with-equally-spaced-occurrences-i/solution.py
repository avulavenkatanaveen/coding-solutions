class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos={}
        for i in range(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]]=[]
            pos[nums[i]].append(i)
        count = 0
        for x in pos:
            if len(pos[x]) == 3:
                a,b,c=pos[x]
                if b-a==c-b:
                    count+=1
        return count