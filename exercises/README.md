# OOP exercise 1: add eval history to oop_dawn.Collaborator

oop_dawn.Collaborator stores the evaluation points in an attribute "evaluation".

But two consecutive calls of Boss.evaluate(c) result in the first value to be overwritten.

Create  a new class MyCollaborator(Collaborator)
which has an attribute `evaluations` that stores ALL the evaluations (a list)

The following code must work:


```python
c = MyCollaborator("pepe")
boss = Boss("Jefez")

assert(issubclass(MyCollaborator, Collaborator))

assert(c.evaluation == None)
assert(len(c.evaluations) == 0)

boss.evaluate(c)
print c.evaluations
assert(len(c.evaluations) == 1)
assert(c.evaluations[-1] == c.evaluation)

boss.evaluate(c)
print c.evaluations
assert(len(c.evaluations) == 2)
assert(c.evaluations[-1] == c.evaluation)
```

# OOP exercise 2: modify the `Collaborator` class to be print-friendly

Right now, a print on a collaborator is not very user-friendly:

```python
In [1]: import oop_dawn

In [2]: c = oop_dawn.Collaborator('Mindundez')

In [3]: print c
<oop_dawn.Collaborator object at 0x7f3427601ed0>
```

Make make it so that the following test passes:

```python
c1 = Collaborator('Mindundez')
c2 = Boss('Jefez')
c3 = SuperBoss('Juan Bueno')

assert(str(c1) == "Mindundez:Collaborator")
assert(str(c2) == "Jefez:Boss")
assert(str(c3) == "Juan Bueno:SuperBoss")
```

Note: you may find the [docs of the special methods](https://docs.python.org/2/reference/datamodel.html#special-method-names
) interesting:


# OOP exercise 3: Create a class `Staff`

Implement the `Staff` class missing in [staff.py](staff.py) so that it passes the tests and conforms to the docs

**Try not to look at the exercises.cheat.oop_dawn_cheat module!!**


# Qt exercise 1: create a basic widget

Run `python exercises/cheat/qtexercise1.py` and try to reproduce it by programming
it yourself. Pay attention to the layouts and the signals.

Notes:
- The widgets are: a QLineEdit, a QPushButton and a QTextBrowser in a QWidget
- Hint: use [qtexample02.py](/docs/qtexample02.py) as a template


# Qt exercise 2: create a basic widget with Qt designer

Do the same as qtexercise01 but using the Qt Designer


# Taurus exercise 1: A simple taurus example with taurusdesigner

Run `python exercises/cheat/taurusexercise1.py --taurus-polling-period=500` and try to reproduce it by programming
it yourself.

Notes:

- Use taurusdesigner to create the ui, and use `UILoader` from `taurus.qt.qtgui.util.ui`
- when running, enter a valid taurusattribute name in the lineEdit (e.g. `eval:rand()`)
  and click the button to set the model to the label in the bottom
- For the .py file, use the following template:
```python
import sys
from taurus.external.qt import QtGui, uic
from taurus.qt.qtgui.application import TaurusApplication


class TaurusExercise1Widget(QtGui.QWidget):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):

        # ...
        # load the UI from <exercises>/ui/TaurusExercise1Widget.ui
        uic.loadUi(...)
        # ...
    
    # ...

if __name__ == "__main__":

    # Initialize a Qt application (Qt will crash if you do not do this first)
    app = TaurusApplication()

    # instantiate the widget
    w = TaurusExercise1Widget()

    # show it (if you do not show the widget, it won't be visible)
    w.show()

    # Initialize the Qt event loop (and exit when we close the app)
    sys.exit(app.exec_())
```
  


# Taurus exercise 2: Taurus-ify an existing widget


 Create a taurus-aware QLabel that accepts an attribute as its model and shows
whether its rvalue is ODD or EVEN (you may assume that rvalue is always an int)

- accepts an attribute as a Model (i.e., inherits from TaurusBaseComponent)
- reacts to new values of the model by setting its own text as follows:
 - if the value is odd, it shows "ODD: <value>"
 - if the value is even, it shows "EVEN <value>"
 - in any other case (e.g. if not an int) it shows "INVALID: <value>"
 - test it using `<widget>.setModel('eval:randint(1,9)')`
 - Hint: you can check if a number is odd with: `int(<number>) % 2`






