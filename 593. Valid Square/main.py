class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        distances = [
            self.distance(p1, p2),
            self.distance(p1, p3),
            self.distance(p1, p4),
            self.distance(p2, p3),
            self.distance(p2, p4),
            self.distance(p3, p4)
        ]
        items = set()
        for distance in distances:
            items.add(distance)

        print(items)

        if len(items) == 3:
            return False
        if len(items) == 2:
            smallest = min(items)
            largest = max(items)
            x = round(2 * pow(smallest, 2),2)
            y = round(pow(largest, 2),2)
            print(x,y)
            if  x ==y:
                return True
            else:
                return False

    def distance(self,point1, point2):
        x =  ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
        return x ** 0.5