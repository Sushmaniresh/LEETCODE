class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        print(graph)
        print(indegree)
        q = deque()
        for course in range(numCourses):
            if indegree[course]==0:
                q.append(course)
        
        visited = 0
        while q:
            visited +=1
            node = q.popleft()
            res.append(node)
            for n in graph[node]:
                indegree[n]-=1
                if indegree[n] == 0:
                    q.append(n)
        
        if visited == numCourses:
            return res
        else:
            return []