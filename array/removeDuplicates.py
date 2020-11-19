# problem: give a sorted list, remove the duplicated element, only return the length

#%%
def removeDuplicated(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    else:
        length = 1
        for i in range (len(nums)):
            if nums[i] != nums[i+1]:
                length+=1
        return length

removeDuplicated([0,1,2])

