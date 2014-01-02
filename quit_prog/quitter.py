#!/usr/bin/env python3

# Copyright (c) 2010-2011, 2013 by Algis Kabaila. 
# This work is made available under  the terms of the 
# Creative Commons Attribution-ShareAlike 3.0 license,
# http://creativecommons.org/licenses/by-sa/3.0/. 

# quitter.py - provide a button to quit this "program"

import sys

from PySide.QtGui import QMainWindow, QPushButton, QApplication

from ui_quitter import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit( app.exec_() )

  
