class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewel_items = list(jewels)
        stone_list = list(stones)
        count = 0
        for item in stone_list:
            if item in jewel_items:
                count += 1
        return count

