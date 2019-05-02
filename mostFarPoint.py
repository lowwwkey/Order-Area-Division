# -*-coding:utf-8-*-

from math import radians, cos, sin, asin, sqrt


class MostFarPoint(object):

    def __init__(self, point_set):
        self.point_set = point_set

    def calculate_distance(self):
        def haversine(x, y):
            """
            Calculate the great circle distance between two points
            on the earth (specified in decimal degrees)

            Args:
            x: [lon1, lat1]
            y: [lon2, lat2]
            """

            lon1, lat1, lon2, lat2 = x[0], x[1], y[0], y[1]
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            r = 6371
            return c * r * 1000

        D = {'point': [0.0, 0.0], 'distance': 0}

        for i in range(len(self.point_set)-1):
            for j in range(i+1, len(self.point_set)):
                dist = haversine(self.point_set[i], self.point_set[j])
                if dist > D['distance']:
                    D.update(point=[self.point_set[i], self.point_set[j]], distance=dist)

        return D


if __name__ == '__main__':
    a = [[0.0, 0.0],
         [1.0, 1.0],
         [1.5, 0.3],
         [0.8, 1.1]]

    b = MostFarPoint(a)
    print(b.calculate_distance())