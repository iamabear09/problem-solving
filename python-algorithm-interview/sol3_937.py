from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        char_logs = []
        digit_logs = []
        
        for log in logs:
            if log.split()[1].isalpha():
                char_logs.append(log)
            else:
                digit_logs.append(log)
        
        char_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return char_logs + digit_logs