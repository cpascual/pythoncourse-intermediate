"""
Create a taurus-aware QLabel that accepts an attribute as its model and shows
whether its rvalue is ODD or EVEN (you may assume that rvalue is always an int)

Test it using `<widget>.setModel('eval:randint(1,9)')`

"""

import sys
from taurus.external.qt import QtGui
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.base import TaurusBaseComponent


class EvenOddLabel(QtGui.QLabel, TaurusBaseComponent):
    """A specialized QLineEdit"""

    def __init__(self, parent=None):
        # call the parent class init
        QtGui.QLabel.__init__(self, 'waiting...', parent=parent)
        TaurusBaseComponent.__init__(self, 'EvenOddLabel')
        self.setMinimumWidth(100)

    def handleEvent(self, evt_src, evt_type, evt_val):
        """reimplemented from TaurusBaseComponent
        """
        # TaurusBaseComponent.handleEvent does nothing, so no need to call it
        try:
            if int(evt_val.rvalue) % 2:  # x % 2 --> 0 if x is even
                prefix = 'ODD'
            else:
                prefix = 'EVEN'
        except:
            prefix = 'INVALID'
            self.warning('Invalid value %s', evt_val.rvalue)

        self.setText('{}: {}'.format(prefix, evt_val.rvalue))


if __name__ == "__main__":

    # Initialize a Qt application (Qt will crash if you do not do this first)
    app = TaurusApplication()

    # instantiate the widget
    w = EvenOddLabel()

    # set the model
    if len(sys.argv) > 1:
        model = sys.argv[1]
    else:
        model = 'eval:randint(1,9)'
        # w.setModel('eval:"foo"')
    w.setModel(model)
    
    # show it (if you do not show the widget, it won't be visible)
    w.show()

    # Initialize the Qt event loop (and exit when we close the app)
    sys.exit(app.exec_())
