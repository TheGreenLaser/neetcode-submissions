class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = []
        
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        target_list = self.map[key]       
        low_bound = 0
        high_bound = len(target_list) - 1

        while high_bound >= low_bound:
            middle = (high_bound+low_bound) // 2
            middle_elem = target_list[middle]

            if middle_elem[0] > timestamp:
                high_bound = middle - 1
            else:
                low_bound = middle + 1
        
        if high_bound < 0:
            return ""
            
        return target_list[high_bound][1]

