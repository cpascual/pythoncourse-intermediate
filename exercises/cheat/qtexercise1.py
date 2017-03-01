"""
exercise 1

"""

import sys
from PyQt4 import QtGui


class MyWidget1(QtGui.QWidget):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):

        # call the parent class init
        QtGui.QWidget.__init__(self, parent=parent)

        # set ui
        self._initUi()

        # connect signals
        self.clearButton.clicked.connect(self.lineEdit.clear)
        self.lineEdit.textChanged.connect(self.textBrowser.setText)

    def _initUi(self):
        """Initialize the GUI elements and layouts"""

        # create the subwidgets
        #   (we could pass them `parent=self` but, because we will add them to
        #    the layout, they will get re-aparented anyway)
        self.lineEdit = QtGui.QLineEdit()
        self.clearButton = QtGui.QPushButton(text="Clear")
        self.textBrowser = QtGui.QTextBrowser()

        # create the layouts
        layout1 = QtGui.QHBoxLayout()
        layout2 = QtGui.QVBoxLayout()

        # fill the layouts
        layout1.addWidget(self.lineEdit)
        layout1.addWidget(self.clearButton)
        layout2.addLayout(layout1)
        layout2.addWidget(self.textBrowser)

        # set the main layout of self
        self.setLayout(layout2)


if __name__ == "__main__":

    # Initialize a Qt application (Qt will crash if you do not do this first)
    app = QtGui.QApplication(sys.argv)

    # instantiate the widget
    w = MyWidget1()

    # show it (if you do not show the widget, it won't be visible)
    w.show()

    # Initialize the Qt event loop (and exit when we close the app)
    sys.exit(app.exec_())
