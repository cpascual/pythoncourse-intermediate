import sys
from taurus.external.qt import QtGui
from taurus.qt.qtgui.application import TaurusApplication


class TaurusExercise1Widget(QtGui.QWidget):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):

        # use taurusexercise1.ui (it defines 3 widgets:
        # - lineEdit, pushButton, taurusLabel
        #
        # make that a button click sets the text of the lineEdit as
        # the taurusLabel model



if __name__ == "__main__":

    # Initialize a Qt application (Qt will crash if you do not do this first)
    app = TaurusApplication()
    # instantiate the widget
    w = TaurusExercise1Widget()
    # show it (if you do not show the widget, it won't be visible)
    w.show()
    # Initialize the Qt event loop (and exit when we close the app)
    sys.exit(app.exec_())
