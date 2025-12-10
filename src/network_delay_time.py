import heapq
from typing import Deque, Dict, List, Tuple


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build adjacency list for source node
        adj = {}
        for u, v, w in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((v, w))

        min_time: Dict[int, float] = {i: float('inf') for i in range(1, n + 1)}
        min_time[k] = 0
        search = Deque([k])
        while search:
            u = search.popleft()

            if u in adj:
                for v, w in adj[u]:
                    new_time = min_time[u] + w

                    if new_time < min_time[v]:
                        min_time[v] = new_time
                        search.append(v)

        max_delay = max(min_time.values())
        return int(max_delay) if max_delay != float('inf') else -1
    

    def networkDelayTime_dijkstra(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 1. 构建邻接表 (Adjacency List)
        # 格式: {源节点: [(目标节点, 权重), ...]}
        adj: Dict[int, List[Tuple[int, int]]] = {}
        for u, v, w in times:
            # 使用 setdefault 简化初始化
            adj.setdefault(u, []).append((v, w))
            
        # 2. 初始化最短距离 (Distance)
        # 存储从 k 到每个节点的最短时间。
        # 节点编号从 1 到 n，所有节点初始化为无穷大。
        min_time: Dict[int, float] = {i: float('inf') for i in range(1, n + 1)}
        min_time[k] = 0
        
        # 3. 初始化优先队列 (Priority Queue)
        # 格式: (时间, 节点)，heapq 是最小堆，时间最短的优先弹出
        pq: List[Tuple[int, int]] = [(0, k)]  # (time_from_k, node_id)
        
        # 4. Dijkstra 主循环
        while pq:
            time_to_u, u = heapq.heappop(pq)
            
            # 如果当前时间 (time_to_u) 大于 min_time[u]，说明已经通过更短的路径处理过 u
            # 这是一个重要的优化，用于跳过过期的堆元素
            if time_to_u > min_time[u]:
                continue
            
            # 遍历节点 u 的所有邻居 v
            if u in adj:
                for v, w in adj[u]:
                    new_time = time_to_u + w
                    
                    # 松弛操作 (Relaxation): 找到从 k 到 v 的更短路径
                    if new_time < min_time[v]:
                        min_time[v] = new_time
                        heapq.heappush(pq, (new_time, v))
                        
        # 5. 结果处理
        
        # 找到所有最短路径中的最大值
        max_delay = max(min_time.values())
        
        # 如果最大延迟时间仍然是无穷大，说明至少有一个节点不可达
        if max_delay == float('inf'):
            return -1
        
        return int(max_delay) # 结果保证是整数