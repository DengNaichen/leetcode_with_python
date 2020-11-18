def twoSum (nums, target):
    reverse = {}
    for i, value in enumerate(nums):
        remaining = target - value
        if remaining not in reverse:
            reverse[value] = i  # the key for dict should be the value
        else:
            return [i, reverse[remaining]]


# # 学到了：
# enumerate 的用法；
# in a dict return the key