# 从 src 目录导入待测试的函数
from src.two_sum import two_sum 

def test_two_sum_basic() -> None:
    """测试基本正向案例"""
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert two_sum(nums, target) == expected

def test_two_sum_different_order():
    """测试结果索引顺序"""
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]

def test_two_sum_duplicates():
    """测试列表中有重复数字的场景"""
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]

def test_two_sum_not_found():
    """测试找不到结果的场景"""
    nums = [1, 2, 3]
    target = 7
    assert two_sum(nums, target) == []