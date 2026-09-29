class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        dq = deque()

        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while len(dq) > 0 and temp > temperatures[dq[-1]]:
                answer[dq[-1]] = i - dq[-1]
                dq.pop()

            dq.append(i)
        
        return answer


        
        