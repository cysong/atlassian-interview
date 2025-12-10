import pytest
from src.closest_bst_value import TreeNode, Solution

def generate_test_data():
    data = []
    root = TreeNode(5, TreeNode(3, TreeNode(1, None, None), TreeNode(4, None, None)), TreeNode(7, None, TreeNode(9, None, None)))
    data.append((root, 5.1, 5))
    data.append((root, 5.0, 5))
    data.append((root, 2.0, 1))
    data.append((root, -2.0, 1))
    data.append((root, 8.7, 9))
    data.append((root, 100, 9))
    data.append((None, 10, None))
    return data

@pytest.mark.parametrize("root, target, expected", generate_test_data())
def test_closest_bst_value(root, target, expected):
    assert Solution().find_closest_value(root, target) == expected