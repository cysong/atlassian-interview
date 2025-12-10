
from src.auto_complete import AutocompleteSystem, AutocompleteSystemTree


def test_autocomplete_system():
    # 场景 1 & 2
    sentences = ["i love you", "island", "i love leetcode"]
    times = [5, 3, 2]
    ac_sys = AutocompleteSystem(sentences, times)

    # 1. 基础查询
    assert ac_sys.input('i') == ["i love you", "island", "i love leetcode"]
    assert ac_sys.input(' ') == ["i love you", "i love leetcode"]

    # 2. 频率更新
    ac_sys.input('l')
    ac_sys.input('o')
    ac_sys.input('v')
    ac_sys.input('e')
    ac_sys.input(' ')
    ac_sys.input('l')
    ac_sys.input('e')
    ac_sys.input('e')
    ac_sys.input('t')
    ac_sys.input('c')
    ac_sys.input('o')
    ac_sys.input('d')
    ac_sys.input('e')
    assert ac_sys.input('#') == [] # 提交 "i love leetcode"，频率更新为 3

    # 验证频率更新后的重排序
    # 初始: i love you(5), island(3), i love leetcode(2)
    # 提交后: i love you(5), island(3), i love leetcode(3)
    # 频率相同按字典序: i love leetcode < island
    assert ac_sys.input('i') == ["i love you", "i love leetcode", "island"] 
    ac_sys.input('s')
    assert ac_sys.input('#') == [] # 提交 "is"，新句子频率为 1
    
    # 验证新句子是否加入
    assert ac_sys.input('i') == ["i love you", "i love leetcode", "island"]
    
    # 3. 字典序 tie-breaking (新实例)
    sentences_3 = ["a", "b", "c"]
    times_3 = [10, 10, 10]
    ac_sys_3 = AutocompleteSystem(sentences_3, times_3)
    
    ac_sys_3.input('a')
    ac_sys_3.input('#') # "a" 频率 11
    ac_sys_3.input('b')
    ac_sys_3.input('#') # "b" 频率 11
    ac_sys_3.input('c')
    ac_sys_3.input('#') # "c" 频率 11
    
    assert ac_sys_3.input('a') == ["a"] # 匹配前缀 "a"
    
    ac_sys_3.input(' ')
    # 期望按字典序排序，且频率最高 (均为 11)
    # 结果: ['a', 'b', 'c'] (因为它们是唯一的匹配项)
    assert ac_sys_3.input('#') == [] # 提交 "a b c"，新句子频率 1
    
    # 验证所有句子排序
    assert ac_sys_3.input('') == ["a", "b", "c"] # 匹配空前缀


def test_autocomplete_system_tree():
    # 场景 1 & 2
    sentences = ["i love you", "island", "i love leetcode"]
    times = [5, 3, 2]
    ac_sys = AutocompleteSystemTree(sentences, times)

    # 1. 基础查询
    assert ac_sys.input('i') == ["i love you", "island", "i love leetcode"]
    assert ac_sys.input(' ') == ["i love you", "i love leetcode"]

    # 2. 频率更新
    ac_sys.input('l')
    ac_sys.input('o')
    ac_sys.input('v')
    ac_sys.input('e')
    ac_sys.input(' ')
    ac_sys.input('l')
    ac_sys.input('e')
    ac_sys.input('e')
    ac_sys.input('t')
    ac_sys.input('c')
    ac_sys.input('o')
    ac_sys.input('d')
    ac_sys.input('e')
    assert ac_sys.input('#') == [] # 提交 "i love leetcode"，频率更新为 3

    # 验证频率更新后的重排序
    # 初始: i love you(5), island(3), i love leetcode(2)
    # 提交后: i love you(5), island(3), i love leetcode(3)
    # 频率相同按字典序: i love leetcode < island
    assert ac_sys.input('i') == ["i love you", "i love leetcode", "island"] 
    ac_sys.input('s')
    assert ac_sys.input('#') == [] # 提交 "is"，新句子频率为 1
    
    # 验证新句子是否加入
    assert ac_sys.input('i') == ["i love you", "i love leetcode", "island"]
    
    # 3. 字典序 tie-breaking (新实例)
    sentences_3 = ["a", "b", "c"]
    times_3 = [10, 10, 10]
    ac_sys_3 = AutocompleteSystem(sentences_3, times_3)
    
    ac_sys_3.input('a')
    ac_sys_3.input('#') # "a" 频率 11
    ac_sys_3.input('b')
    ac_sys_3.input('#') # "b" 频率 11
    ac_sys_3.input('c')
    ac_sys_3.input('#') # "c" 频率 11
    
    assert ac_sys_3.input('a') == ["a"] # 匹配前缀 "a"
    
    ac_sys_3.input(' ')
    # 期望按字典序排序，且频率最高 (均为 11)
    # 结果: ['a', 'b', 'c'] (因为它们是唯一的匹配项)
    assert ac_sys_3.input('#') == [] # 提交 "a b c"，新句子频率 1
    
    # 验证所有句子排序
    assert ac_sys_3.input('') == ["a", "b", "c"] # 匹配空前缀