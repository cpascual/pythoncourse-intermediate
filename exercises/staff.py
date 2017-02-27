"""
Implement a Staff class that acts as a group (a sequence) of Collaborators.
It should be possible to :

- add new collaborators with `staff.add_collaborator()`
- get a numpy array containing the salaries of all collaborators (`salaries`)
- provide the number of collaborators when used with `len(staff)`

"""
import numpy as np
from exercises.cheat.oop_dawn_cheat import Collaborator, Boss, SuperBoss


# implement the Staff class here


def test():
    staff = Staff()
    for i in range(1,9):
        name = "minion%i" % i
        salary = i*10000
        staff.add_collaborator(Collaborator(name, salary))

    # print len(staff), staff.salaries.sum()
    try:
        assert len(staff) == 8
        assert np.all(staff.salaries == np.arange(10000,90000,10000))
        print "SUCCESS!!!"
    except Exception, e:
        print "FAILED!!"
        raise e

if __name__ == "__main__":
    test()