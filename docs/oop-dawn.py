"""A salaries simulator for a totally fictional reasearch Lab"""

import numpy as np


class Collaborator(object):
    """A worker, in HR-talk """

    POINTS_FOR_PROMOTION = 22.5
    average_points = 7
    avg_salary = 29000

    def __init__(self, name, base_salary=None):
        self.name = name
        if base_salary is None:
            base_salary = np.random.normal(loc=self.avg_salary,
                                           scale= 0.1 * self.avg_salary)
        self.base_salary = base_salary
        self.evaluations = []

    def calculate_bonus(self):
        if self.evaluations:
            return 0.04 * self.base_salary * self.evaluations[-1] / 10.
        else:
            return 0

    def salary(self):
        promotions = np.floor(np.sum(self.evaluations) /
                              self.POINTS_FOR_PROMOTION)
        return self.base_salary * (1 + 0.05 * promotions)

    def add_evaluation(self, points=None):
        if points is None:
            points = min(10, np.random.normal(loc=self.average_points, scale=2))
        self.evaluations.append(points)


class Boss(Collaborator):
    """Big boss"""
    average_points = 9
    avg_salary = 70000


class SuperBoss(Collaborator):
    """The Uber-boss"""

    def calculate_bonus(self):
        return 12000


class Mineco(Collaborator):
    """The poor ministry grant-holder"""
    avg_salary = 16000

    def add_evaluation(self, *args, **kwargs):
        pass


class Staff(list):

    def replace_collabs(self, n):
        """ pick up n  collaborators and replace them by "newcomers" """
        for _ in range(n):
            i = np.random.randint(0, len(all_staff))  # choose them randomly
            c = all_staff[i]
            klass = type(c)
            name = self.random_name()
            base_salary = c.base_salary * 0.8  # "you know... the crisis..."
            all_staff[i] = klass(name, base_salary)

    def add_collabs(self, n, klass):
        for _ in range(n):
            self.append(klass(self.random_name()))

    def get_data(self):
        salaries = np.array([c.salary() for c in self])
        base_salaries = np.array([c.base_salary for c in self])
        bonuses = np.array([c.calculate_bonus() for c in self])
        return salaries, base_salaries, bonuses

    def print_stats(self):
        stats = self.get_data()
        print "STAT\tsalary\tbase\tbonus"
        print "mean\t{:5g}\t{:5g}\t{:g}".format(*[s.mean() for s in stats])
        print "Number of staff:", len(all_staff)

    @staticmethod
    def random_name():
        """
        :return: random initials
        """
        letters = tuple("ABCDEFGHIJKLMNOPQRSTUVWYZ")
        _name = np.random.choice(letters)
        _surname = np.random.choice(letters)
        return "{}.{}.".format(_name, _surname)


if __name__ == "__main__":

    from matplotlib import pyplot as plt

    plt.axis([0, 12000, 0, 70])
    plt.ion()
    plt.show()

    all_staff = Staff()
    all_staff.append(SuperBoss(all_staff.random_name(), 100000))
    all_staff.add_collabs(9, Boss)

    for year in range(2002, 2018):
        np.random.seed(1234)
        # do evaluations:
        for c in all_staff:
            c.add_evaluation()

        # pick up to 30% collaborators and replace them by "newcomers"
        n = np.random.randint(0, int(0.3 * len(all_staff)))
        all_staff.replace_collabs(n)

        # increase staff
        n = np.random.randint(0, 20)
        all_staff.add_collabs(n, Collaborator)
        if year>2014:
            all_staff.add_collabs(5, Mineco)

        print "\n----- ", year
        all_staff.print_stats()
        sal, base, bonus = all_staff.get_data()

        plt.cla()
        plt.axis([None, None, 0, 70])
        plt.hist(bonus, bins=100)
        plt.draw()
        plt.pause(0.001)

    raw_input("press Enter to exit")





