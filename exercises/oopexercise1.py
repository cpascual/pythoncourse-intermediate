"""OOP examples using staff categories"""

import numpy as np


class Collaborator(object):
    """A worker, in HR-talk
    It holds a name, a base_salary and evaluation points.
    It can calculate its own salary and bonus.
    """

    avg_salary = 29000

    def __init__(self, name, base_salary=None):
        self.name = name
        if base_salary is None:
            base_salary = np.random.normal(loc=self.avg_salary,
                                           scale= 0.1 * self.avg_salary)
        self.base_salary = base_salary
        self._evaluation = None

    def get_evaluation(self):
        return self._evaluation

    def set_evaluation(self, points):
        self._evaluation = min(10, points)

    @property
    def bonus(self):
        """returns the bonus for this year"""
        points = self.evaluation
        if points is None:
            return 0
        else:
            return 0.04 * self.base_salary * points / 10.

    @property
    def salary(self):
        """returns salary considering base_salary and bonus"""
        return self.base_salary + self.bonus


class Boss(Collaborator):
    """Big boss"""

    avg_salary = 80000

    @staticmethod
    def evaluate(collab):
        points = min(10, np.random.normal(loc=7, scale=2))
        collab.set_evaluation(points)


class SuperBoss(Boss):
    """The Uber-boss"""

    avg_salary = 100000
    base_salary = avg_salary
    bonus = 12000
    salary = base_salary + bonus


class MyCollaborator(Collaborator):

    pass  # Add your implementation here


if __name__ == "__main__":
    print(1)
    c = MyCollaborator("pepe")
    print(2)
    boss = Boss("Jefez")
    print(3)
    assert (issubclass(MyCollaborator, Collaborator))
    print(4)
    assert (c.evaluation == None)
    print(5)
    assert (len(c.evaluations) == 0)
    print(6)
    boss.evaluate(c)
    print (c.evaluations)
    assert (len(c.evaluations) == 1)
    print(7)
    assert (c.evaluations[-1] == c.evaluation)
    print(8)
    boss.evaluate(c)
    print (c.evaluations)
    assert (len(c.evaluations) == 2)
    assert (c.evaluations[-1] == c.evaluation)
    print(9)
