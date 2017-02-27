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
        self.evaluation = None

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
        collab.evaluation = points


class SuperBoss(Boss):
    """The Uber-boss"""

    avg_salary = 100000
    base_salary = avg_salary
    bonus = 12000
    salary = base_salary + bonus


def test_1():
    np.random.seed(12345)
    c1 = Collaborator("Mindundez", 22000)
    c2 = Boss("Jefez")
    c3 = SuperBoss("Juan Bueno")

    for c in c1, c2, c3:
        print "{c.name} ({c.__class__.__name__}) {c.salary:.0f}eur".format(c=c)

    print
    print "before eval"
    print c1.evaluation, c1.bonus, c1.salary
    c2.evaluate(c1)
    print "after eval"
    print c1.evaluation, c1.bonus, c1.salary

if __name__ == "__main__":

    test_1()
