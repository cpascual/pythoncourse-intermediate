"""
Same as example01.py, but using Object-Oriented Programming

"""

import sys
from PyQt4 import QtGui


class MyEdit(QtGui.QLineEdit):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):

        # call the parent class init
        QtGui.QLineEdit.__init__(self, parent=parent)

        # connect signal
        self.textEdited.connect(self.printText)

        # call a method of the parent
        self.setText('This is a {:s}'.format(self.__class__.__name__))

    def printText(self, text):
        """
        Prints the given text

        :param text: (str)
        """
        print text


if __name__ == "__main__":

    # Initialize a Qt application (Qt will crash if you do not do this first)
    app = QtGui.QApplication(sys.argv)

    # instantiate the widget
    w = MyEdit()

    # show it (if you do not show the widget, it won't be visible)
    w.show()

    # Initialize the Qt event loop (and exit when we close the app)
    sys.exit(app.exec_())
