"""
Qt exercise 2 (solved in )

"""

import os
import sys
from PyQt4 import QtGui, uic  


class MyWidget2(QtGui.QWidget):
    """A specialized QLineEdit (implemented using signal connections declared
    in the loaded .ui file)
    """

    def __init__(self, parent=None):

        # call the parent class init
        QtGui.QWidget.__init__(self, parent=parent)

        # get the absolute path to `ui/MyWidget2.ui` and load it into self
        # Note: this .ui includes signal connections!
        uipath = os.path.join(os.path.dirname(__file__), 'ui', 'MyWidget2.ui')
        uic.loadUi(uipath, self) 


class MyWidget2b(QtGui.QWidget):
    """A specialized QLineEdit (alternative implementation connecting signals 
    in this .py file)
    """

    def __init__(self, parent=None):

        # call the parent class init
        QtGui.QWidget.__init__(self, parent=parent)

        # get the absolute path to `ui/MyWidget2b.ui` and load it into self
        # Note: this .ui *does not* include signal connections!
        uipath = os.path.join(os.path.dirname(__file__), 'ui', 'MyWidget2b.ui')
        uic.loadUi(uipath, self)  

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
