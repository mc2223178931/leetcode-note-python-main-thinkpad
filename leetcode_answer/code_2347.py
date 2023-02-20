from typing import List

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suit_set=set(suits)
        if len(suit_set) == 1:
            return "Flush"
        count_map = {}
        for rank in ranks:
            if rank in count_map:
                count_map[rank] += 1
            else:
                count_map[rank] = 1
        max_count = 0
        for i in count_map:
            max_count = max(max_count, count_map[i])
        if max_count == 0:
            return "High Card"
        elif max_count == 2:
            return "Pair"
        elif max_count == 3:
            return "Three of a Kind"

if __name__ == "__main__":
    solution = Solution()
    # ranks = [13, 2, 3, 1, 9]
    # suits = ["a", "a", "a", "a", "a"]
    ranks = [10, 10, 2, 12, 9]
    suits = ["a", "b", "c", "a", "d"]
    print(solution.bestHand(ranks, suits))
