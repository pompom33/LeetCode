class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # 1. 해당 룹에서 몇명이 티켓을 사야하는지 구한다
        # 2. 해당 룹에서 걸린 시간을 구한다
        # 3. 더이상 티켓을 사지 않는 사람은 딕셔너리 형태로 티켓 사는데에 걸린 시간 append
        count_dict = {}
        time = 0
        for i in range(max(tickets)):
            for j in range(len(tickets)):
                if j not in count_dict.keys():
                    count_dict[j] = 0             
                if tickets[j] != 0:
                    tickets[j] -= 1
                    time += 1
                    count_dict[j] = time     
        return count_dict[k]