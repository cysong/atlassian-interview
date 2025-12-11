'''
Atlassian runs a lot of CI pipelines and our team is tasked to  build some reporting on the usage to find some cost optimisation patterns.
Each CI pipeline starts at a given time X and ends at Y. We are given a list of CI pipeline time windows {X,Y}.
[{X,Y}, {X, Y}, ….]
Each CI pipeline starts at a given time X and ends at Y. We are given a list of CI pipeline time windows {X,Y}. We want to find the  list of non-overlapping time intervals where at least one CI pipeline is running.

Input: [{2, 5}, {12, 15}, {4, 8}]
Output: [{2, 8}, {12, 15}]

Explanation: The windows in minimum where at least one job is running are {2, 8} and {12, 15}
'''

from typing import List


class Solution:

    def __init__(self, windows: List[tuple]):
        self.windows = windows

    def output(self) -> List[tuple]:
        if not self.windows:
            return []
        self.windows.sort()
        result: List[tuple] = []
        prev: tuple = self.windows[0]
        for i in range(1, len(self.windows)):
            if prev[1] >= self.windows[i][0]:
                prev = (prev[0], max(prev[1], self.windows[i][1]))
            else:
                result.append(prev)
                prev = self.windows[i]
        result.append(prev)
        return result
