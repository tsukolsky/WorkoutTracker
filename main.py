#!/usr/bin/env python

from CustomWidgets import WorkoutTracker
from PyQt4.QtGui import QApplication
import sys

if __name__ == "__main__":
    print "Time to play!"
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    myTracker = WorkoutTracker()
    myTracker.show()
    app.exec_()