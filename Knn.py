from math import sqrt
from typing import Dict, List


class Point(object):
    def __init__(self, x: int, y: int, pclass="none") -> None:
        self._x = x
        self._y = y
        self._pclass = pclass

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def pclass(self) -> str:
        return self._pclass

    @pclass.setter
    def pclass(self, value):
        self._pclass = value

    def __str__(self) -> str:
        return f'(x: {self.x}, y: {self.y}, class = {self._pclass})'

    def __repr__(self) -> str:
        return f'(x: {self.x}, y: {self.y}, class = {self._pclass})'


class Classifier(object):
    def __init__(self, pointlist: List, predict: Point, radius: float) -> None:
        self._pointlist = pointlist
        self._predict = predict
        self._radius = radius

    def distance(self, point: Point) -> float:
        return sqrt((self._predict.x - point.x) ** 2 + (self._predict.y - point.y) ** 2)

    def classify(self) -> str:
        print(f'Data: \n{"\n".join(map(str, self._pointlist))},\npredict:\n{self._predict}')
        finalClass: str
        distances: Dict[Point, float] = dict()
        classes: Dict[str, int] = dict()
        for i in self._pointlist:
            dis_temp = self.distance(i)
            if dis_temp < self._radius:
                distances[i] = dis_temp
                if i.pclass in classes.keys():
                    classes[i.pclass] += 1
                else:
                    classes[i.pclass] = 1
        if len(classes) == 0:
            return "noneOfClass"

        min_dist = (list(classes.keys())[0], 0.0)
        for i in classes.keys():
            if classes[i] > min_dist[1]:
                min_dist = (i, classes[i])
        self._predict.pclass = min_dist[0]
        return min_dist[0]
