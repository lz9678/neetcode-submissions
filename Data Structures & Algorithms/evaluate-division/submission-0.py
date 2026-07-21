import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. create graph
        # { 'A': {'B': 2.0, 'C': 3.0}, 'B': {'A': 0.5} ... }
        # key是node；value 是连接的node 以及division的值
        graph = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            graph[num][den] = val
            graph[den][num] = 1.0/val

        # 2. 定义 BFS 寻路函数
        def bfs(start, end):
            # 如果查询的节点不存在于equation中，直接返回 -1.0
            if start not in graph or end not in graph:
                return -1.0
            
            # 初始化FIFO queue，里面存的是 (当前节点, 到达该节点时的累乘值)
            queue = collections.deque([(start, 1.0)])
            
            # 使用集合记录访问过的节点，防止遇到环导致死循环
            visited = set([start])
            
            # 只要queue里还有没探索的节点，就继续探索。
            while queue:
                # popleft() 会把queue最前面的叫出来FIFO
                curr_node, curr_val = queue.popleft()
                
                # 找到目标节点，返回累乘结果
                if curr_node == end:
                    return curr_val
                
                # 如果当前节点不是终点，那就看看它四周有哪些邻居（找下一层的路）。
                # 遍历相邻的节点
                for neighbor, weight in graph[curr_node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_val * weight))
            
            # 如果把连通分支都找遍了还是没找到目标节点，说明不连通
            return -1.0
            
        # 3. 遍历查询，收集所有结果
        result = []
        for c, d in queries:
            result.append(bfs(c, d))
            
        return result