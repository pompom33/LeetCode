class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        i = 1
        visited = {1}
        cur_loc = 1
        while True:
            new_loc = (cur_loc + i * k) % n
            if new_loc == 0:
                new_loc = n
            if new_loc in visited:
                break
            visited.add(new_loc)
            i += 1
            cur_loc = new_loc
        n_set = set([x+1 for x in range(n)])
        return sorted(list(n_set - visited))