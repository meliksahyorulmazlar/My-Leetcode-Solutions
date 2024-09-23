class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        common = [r for r in list1 if r in list2]

        item = common[0]
        items = [item]
        index = list1.index(item) + list2.index(item)

        for rating in common[1:]:
            new_index = list1.index(rating) + list2.index(rating)
            if new_index < index:
                items = []
                items.append(rating)
                index = new_index
            elif new_index == index:
                items.append(rating)

        return items
