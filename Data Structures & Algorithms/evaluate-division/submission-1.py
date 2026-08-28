class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 把变量看成图里的节点，把除法关系看成带权边。
        # a / b = 2
        # b / c = 3
        # 可以画成 a --2--> b --3--> c
        # 同时反方向就是
        # b --1/2--> a
        # c --1/3--> b
        from collections import defaultdict
        graph = defaultdict(list)

        for (a,b), val in zip(equations, values):
            # graph["a"] = [("b", val)] 表示 a / b = val
            graph[a].append((b, val))
            graph[b].append((a, 1/val))

        # DFS: 从 a 出发，先挑一条路一直往深处走，看看能不能找到 c。
        def dfs(cur: str, target: str, product: float, visited: set):
            if cur == target:
                return product
            
            visited.add(cur)

            for neighbor, weight in graph[cur]:
                if neighbor not in visited:
                    result = dfs(neighbor, target, product * weight, visited)
                    if result != -1.0:
                        return result
            return -1.0
        
        res = []                   
        for start, target in queries:
            if start not in graph or target not in graph:
                res.append(-1.0)
                continue

            answer = dfs(start, target, 1.0, set())

            res.append(answer)

        return res
            
            
            




        