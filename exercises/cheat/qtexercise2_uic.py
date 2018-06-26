"""
qt exercise 2 (without using uiload)

Redo qtexercise2 but using the PyQt4.uic module directly

My previous solutions for solving qtexercise2 involved using the UILoadable
decorator which is part of Taurus (or needs to be imported from the uiload
non-standard uiload module.

During the course, it was suggested that the PyQt4.uic module could be used
directly, and I wanted to test it. It seems that the same can indeed be
achieved this way, (see qtexercise2_uic.py) so it seems reasonable to
recommend it over the UILoadable approach .

"""

import sys
import os
from PyQt4 import QtGui, uic  
# NOTE: If you are using taurus, import from taurus.external.qt instead:
# from taurus.external.qt import QtGui, uic


class MyWidget3(QtGui.QWidget):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):

        # call the parent class init
        QtGui.QWidget.__init__(self, parent=parent)

        uipath = os.path.join(os.path.dirname(__file__), 'ui', 'MyWidget2b.ui')
        uic.loadUi(uipath, self)  # simpler recipe than using uiload

        # connect signals  (IMPORTANT: check the object names in the .ui!)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.lineEdit.textChanged.connect(self.textBrowser.setText)


if __name__ == "__main__":

    # Initialize a Qt application (Qt will crash if you do not do this first)
    app = QtGui.QApplication(sys.argv)

    # instantiate the widget
    w = MyWidget3()

    # show it (if you do not show the widget, it won't be visible)
    w.show()

    # Initialize the Qt event loop (and exit when we close the app)
    sys.exit(app.exec_())
