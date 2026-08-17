class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict={}
        for i in arr:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        lucky_num=-1
        for i,freq in dict.items():
            if i==freq:
                if i>lucky_num:
                    lucky_num=i
        return lucky_num
        