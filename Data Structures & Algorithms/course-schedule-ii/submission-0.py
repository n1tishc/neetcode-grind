class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        # Create an ADJ matrix of all course
        pre_matrix = { course: [] for course in range(numCourses)}

        for course, pre in prereq:
            pre_matrix[course].append(pre)
        

        # Theres 3 steps for traversal
        # Visited -> course added to o/p
        # Visiting -> cycle check
        # Unvisited -> Not ayet added anywhere

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            # Base Cases
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)

            for pre in pre_matrix[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output
            