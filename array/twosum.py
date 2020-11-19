def twosum(nums, target):
    store_index = {}
    for i, value in enumerate(nums):
        remaining = target - value
        if remaining not in store_index:
            store_index[value] = i
        else:
            return [i, store_index[remaining]]