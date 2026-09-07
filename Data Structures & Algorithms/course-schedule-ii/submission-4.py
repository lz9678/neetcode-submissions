
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for (a,b) in prerequisites:
            # to take a you need to take b first
            # b => a
            graph[b].append(a)  
            # add one prerequistie for a
            indegree[a] += 1
        
        queue = deque()
        for course in range(numCourses):
            # any course without prerequities can be the start point
            if indegree[course] == 0:
                queue.append(course)

        result = []
        while queue:
            # add the starting course to the result
            course = queue.popleft()
            result.append(course)

            # remove this course from the prerequistie for all relevant courses
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        if len(result) == numCourses:
            return result

        return []



        
                

    


        