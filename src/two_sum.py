def two_sum(nums: list[int], target: int) -> list[int]:
    """
    在一个列表中找到两个数字，它们的和等于目标值。
    返回这两个数字的索引。
    """
    num_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return []