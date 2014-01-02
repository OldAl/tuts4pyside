#!/usr/bin/env python3

# Copyright (c) 2010-2011, 2013 Algis Kabaila. All rights reserved.
# This work is made available under  the terms of the 
# Creative Commons Attribution-ShareAlike 3.0 license,
# http://creativecommons.org/licenses/by-sa/3.0/. 

# licence.py - this small program reads and displays licence details.

import sys

from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton

from ui_licence import Ui_MainWindow

__version__ = '3.3.0'

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        '''Mandatory initialisation of a class.'''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.showButton.clicked.connect(self.fileRead)
        
    def fileRead(self):
        '''Read and display licence.'''
        with open('CCPL.txt') as nonamefile:
            self.textEdit.setText(nonamefile.read())
#        self.textEdit.setText(open('CCAtributionLicence.txt').read())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
    
