class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque

        dq = deque()

        for i in range(len(tokens)):
            val = tokens[i]
            if val == "+" or val == "-" or val == "*" or val == "/":
                val1 = int(dq.pop())
                val2 = int(dq.pop())

                if val == "+":
                    val2 += val1
                elif val == "-":
                    val2 -= val1
                elif val == "*":
                    val2 *= val1
                elif val == "/":
                    val2 = int(val2 / val1)

                dq.append(val2)
                #print(val1)

            else:
                dq.append(val)
                #print(val)
        
        answer = dq.pop()
        return int(answer)





           

        
