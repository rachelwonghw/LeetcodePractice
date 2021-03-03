import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = {}
        result = []
        for item in items:
            if item[0] not in students.keys():
                students[item[0]] = []
            heapq.heappush(students[item[0]], item[1]*-1)
            
            
        for key in students.keys():
            average = 0
            for i in range(0,5):
                grade = heapq.heappop(students[key])
                average += grade*-1
            result.append([key, int(average/5)])
        result.sort(key=lambda item: item[0])
        return result