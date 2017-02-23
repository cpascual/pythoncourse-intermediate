"""
A simple example (programmed procedurally)

See PyQt4 Docs:
 http://pyqt.sourceforge.net/Docs/PyQt4/introduction.html
 http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

Note: the C++ Qt class reference can be more usable than the PyQt4 one:
 http://doc.qt.io/qt-4.8/classes.html

"""

import sys
from PyQt4 import QtGui


def printText(text):
    """a dummy function to be used as a slot for a connection"""
    print text


# Initialize a Qt application (Qt will crash if you do not do this first)
app = QtGui.QApplication(sys.argv)

# instantiate a widget (note that QLineEdit inherits QWidget)
w = QtGui.QLineEdit()

# connect signal
w.textChanged.connect(printText)

# call a method of the widget
w.setText('This is a PyQt4.QtGui.QLabel widget')

# show it (if you do not show the widget, it won't be visible)
w.show()

# Initialize the Qt event loop (and exit when we close the app)
sys.exit(app.exec_())
