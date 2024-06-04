class Solution(object):
    def nearestValidPoint(self, x, y, points):
        distances = []
        indices = []
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                distance = abs(x-points[i][0])+abs(y-points[i][1])
                distances.append(distance)
                indices.append(i)
        if len(distances) == 0:
            return -1
        else:
            smallest = min(distances)
            index = indices[distances.index(smallest)]
            return index