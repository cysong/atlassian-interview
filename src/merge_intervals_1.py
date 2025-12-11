'''
Atlassian runs a lot of CI pipelines and our team is tasked to  build some reporting on the usage to find some cost optimisation patterns.
Each CI pipeline starts at a given time X and ends at Y. We are given a list of CI pipeline time intervals {X,Y}.
[{X,Y}, {X, Y}, ….]
Each CI pipeline starts at a given time X and ends at Y. We are given a list of CI pipeline time intervals {X,Y}. We want to find the  list of non-overlapping time intervals where at least one CI pipeline is running.

Input: [{2, 5}, {12, 15}, {4, 8}]
Output: [{2, 8}, {12, 15}]

Explanation: The intervals in minimum where at least one job is running are {2, 8} and {12, 15}
'''

from typing import List, Tuple

Interval = Tuple[int, int]

class Solution:

    def __init__(self, intervals: List[Interval]):
        self.intervals = intervals

    def merge(self) -> List[Interval]:
        if not self.intervals:
            return []
        self.intervals.sort()
        result: List[Interval] = []
        curr_s, curr_e = self.intervals[0]
        for s, e in self.intervals[1:]:
            if curr_e >= s:
                curr_s, curr_e = curr_s, max(curr_e, e)
            else:
                result.append((curr_s, curr_e))
                curr_s, curr_e = s, e
        result.append((curr_s, curr_e))
        return result
