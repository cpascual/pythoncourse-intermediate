"""
exercise 1

"""

import sys
from PyQt4 import QtGui
from uiload import UILoadable


@UILoadable()
class MyWidget2(QtGui.QWidget):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):

        # call the parent class init
        QtGui.QWidget.__init__(self, parent=parent)

        # set ui (this will load `ui/MyWidget2.ui`)
        # Note: this .ui includes signal connections!
        self.loadUi()


@UILoadable()
class MyWidget2b(QtGui.QWidget):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):

        # call the parent class init
        QtGui.QWidget.__init__(self, parent=parent)

        # set ui (this will load `ui/MyWidget2b.ui`)
        # Note: this ui does *not* include any signal connection
        self.loadUi()

        # connect signals  (IMPORTANT: check the object names in the .ui!)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.lineEdit.textChanged.connect(self.textBrowser.setText)


if __name__ == "__main__":

    # Initialize a Qt application (Qt will crash if you do not do this first)
    app = QtGui.QApplication(sys.argv)

    # instantiate the widget
    w = MyWidget2b()

    # show it (if you do not show the widget, it won't be visible)
    w.show()

    # Initialize the Qt event loop (and exit when we close the app)
    sys.exit(app.exec_())
