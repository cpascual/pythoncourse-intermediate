"""A salaries simulator for a totally fictional research Lab"""

import numpy as np


class Collaborator(object):
    """A worker, in HR-talk
    It holds a name, a base_salary and evaluation points.
    It can calculate its own salary and bonus.
    """

    avg_salary = 29000
    POINTS_FOR_PROMOTION = 22.5
    average_points = 7

    def __init__(self, name, base_salary=None):
        self.name = name
        if base_salary is None:
            base_salary = np.random.normal(loc=self.avg_salary,
                                           scale= 0.1 * self.avg_salary)
        self.base_salary = base_salary
        self._evaluations = []

    def __str__(self):
        return "{s.name:}:{s.__class__.__name__}".format(s=self)

    def get_evaluation(self, i=-1):
        """returns its ith evaluation (the last if i is not passed) or None if
        never evaluated"""
        if self._evaluations:
            return self._evaluations[-1]
        else:
            return None

    def add_evaluation(self, points):
        """adds a new evaluation (points) to the evaluations log
        :param points: points to be added.
        """
        self._evaluations.append(points)

    # "evaluation" property
    evaluation = property(fget=get_evaluation, fset=add_evaluation)

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
        """returns salary considering base_salary, promotions and bonus"""
        promotions = int(np.sum(self._evaluations) / self.POINTS_FOR_PROMOTION)
        return self.base_salary * (1 + 0.05 * promotions) + self.bonus


class Boss(Collaborator):
    """Big boss"""

    average_points = 9
    avg_salary = 80000

    @staticmethod
    def evaluate(collab):
        """Sets the evaluation attribute of a given collaborator to a
        some points
        """
        points = min(10, np.random.normal(loc=collab.average_points, scale=2))
        collab.evaluation = points


class SuperBoss(Boss):
    """The Uber-boss"""

    avg_salary = 100000
    base_salary = avg_salary
    bonus = 12000
    salary = base_salary + bonus


class Mineco(object):
    """The poor ministry grant-holder.  Not actually a Collaborator!!!
    (just duck-typing)
    """

    def __init__(self, name):
        self.name = name
        self.salary = 16000
        self.base_salary = 16000
        self.bonus = 0
        self.evaluation = 0
        self.average_points = 0



class Staff(list):
    """A class that holds a list of collaborators
    """

    def replace_collabs(self, n):
        """ pick up n  collaborators and replace them by "newcomers" """
        for _ in range(n):
            i = np.random.randint(1, len(self))  # choose them randomly
            c = self[i]
            klass = type(c)
            name = self.random_name()
            base_salary = c.base_salary * 0.8  # "you know... the crisis..."
            self[i] = klass(name, base_salary)
        return

    def add_collabs(self, klass, n=1):
        """ add `n` collabs of type `klass` """
        for _ in range(n):
            self.append(klass(self.random_name()))

    def add_collaborator(self, collab):
        """append a new collaborator"""
        self.append(collab)

    def simulate_year(self, repl=0, new=()):
        """
        :param repl: number of collaborators being replaced
        :param new: new open positions (sequence of collaborator classes)
        """
        # do evaluations:
        for c in self:
            Boss.evaluate(c)

        # do replacements
        all_staff.replace_collabs(repl)

        # increase staff
        for k in new:
            self.add_collabs(k)

    @property
    def salaries(self):
        return np.array([c.salary for c in self])

    @property
    def base_salaries(self):
        return np.array([c.base_salary for c in self])

    @property
    def bonuses(self):
        return np.array([c.bonus for c in self])

    def print_stats(self):
        print "Number of staff:", len(self)
        print "mean salary: ", self.salaries.mean()
        print "mean base salary: ", self.base_salaries.mean()
        print "mean bonus: ", self.bonuses.mean()

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

    np.random.seed(1234)

    all_staff = Staff()
    all_staff.append(SuperBoss(all_staff.random_name(), 100000))
    all_staff.add_collabs(Boss, 9)

    for c in all_staff:
        print c

    for year in range(2002, 2018):
        new_pos = [Collaborator]*10
        if year > 2014:
            new_pos += [Mineco]*3

        repl = int(0.1 * len(all_staff))
        all_staff.simulate_year(repl=repl, new=new_pos)

        print "\n----- ", year
        all_staff.print_stats()

    # plot
    # import pyqtgraph as pg
    # win = pg.GraphicsWindow()
    # for i, attr in enumerate(("bonuses", "salaries", "base_salaries")):
    #     plt = win.addPlot(row=i, col=0, title=attr)
    #     h, bins = np.histogram(getattr(all_staff, attr), bins=100)
    #     plt.plot(bins, h, stepMode=True, fillLevel=0, brush="b")
    # raw_input("press Enter to exit")





