from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        res = []
        course_map = defaultdict(list)
        indegree = [0]*numCourses

        for req in prerequisites:
            course_map[req[1]].append(req[0]) 
            indegree[req[0]] += 1
            # to take 0, you need to take 1 first: 1->0
            # key is 1
            # item is 0

        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            current = queue.popleft()
            for item in course_map[current]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)

            res.append(current)

        return res if len(res) == numCourses else []
            