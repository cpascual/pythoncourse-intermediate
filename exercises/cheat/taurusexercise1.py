"""
taurus exercise 1

Show a line edit, a button and a TarusLabel. The user should be able to 
type an attribute name in the LineEdit and, When clicking the button,
the TaurusLabel should show value of that attribute.

"""

import sys
from taurus.external.qt import QtGui
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.util.ui import UILoadable

@UILoadable
class TaurusExercise1Widget(QtGui.QWidget):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):

        # call the parent class init
        QtGui.QWidget.__init__(self, parent=parent)

        # load the UI from ui/TaurusExercise1Widget.ui
        self.loadUi()

        # connect signals  (IMPORTANT: check the object names in the .ui!)
        self.pushButton.clicked.connect(self.onShow)

    def onShow(self):
        self.taurusLabel.setModel(self.lineEdit.text())


if __name__ == "__main__":

    # Initialize a Qt application (Qt will crash if you do not do this first)
    app = TaurusApplication()

    # instantiate the widget
    w = TaurusExercise1Widget()

    # show it (if you do not show the widget, it won't be visible)
    w.show()

    # Initialize the Qt event loop (and exit when we close the app)
    sys.exit(app.exec_())
