def twoSum(nums: list[int], target: int) -> list[int]:
    for index, num in enumerate(nums):
        new_target = target - num
        for add_index, add_num in enumerate(nums[index+1:]):
            if add_num == new_target:
                return [index, add_index+(index+1)]