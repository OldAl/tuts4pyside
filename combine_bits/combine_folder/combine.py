#!/usr/bin/env python3

# Copyright (c) 2010-2011, 2013 by Algis Kabaila. 
# This work is made available under  the terms of the 
# Creative Commons Attribution-ShareAlike 3.0 license,
# http://creativecommons.org/licenses/by-sa/3.0/. 

# combine.py - combination of ShowGPL, About, Close scripts

import sys
import platform

import PySide

from PySide.QtGui import (QApplication, QMainWindow, QMessageBox,  QIcon)

__version__ = '3.1.4'

from ui_combine import Ui_MainWindow

# from . import qrc_combine
import qrc_combine

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Combine Code Blocks.')
        self.actionShow_CCPL.triggered.connect(self.showCCPL)
        self.action_About.triggered.connect(self.about)                
        iconToolBar = self.addToolBar('') 
#------------------------------------------------------
# Add icons to appear in tool bar - step 1
        self.actionShow_CCPL.setIcon(QIcon(":/showgpl.png"))
        self.action_About.setIcon(QIcon(":/about.png"))
        self.action_Close.setIcon(QIcon(":/quit.png"))
#------------------------------------------------------
# Show a tip on the Status Bar - step 2
        self.actionShow_CCPL.setStatusTip("Show CCP Licence")
        self.action_About.setStatusTip("Pop up the About dialog.")
        self.action_Close.setStatusTip("Close the program.")
#------------------------------------------------------        
        iconToolBar.addAction(self.actionShow_CCPL)
        iconToolBar.addAction(self.action_About)
        iconToolBar.addAction(self.action_Close)
        
    def showCCPL(self):
        'Read and display CCPL licence.'
        with open('CCPL.txt') as fi:                  
            self.textEdit.setText(fi.read())        
        
    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PySide, Platform and version.",
                """<b> about.py version %s </b> 
                <p>Copyright &copy; 2013 by Algis Kabaila. 
                This work is made available under  the terms of
                Creative Commons Attribution-ShareAlike 3.0 license,
                http://creativecommons.org/licenses/by-sa/3.0/.
                <p>This application is useful for displaying  
                Qt version and other details.
                <p>Python %s -  PySide version %s - Qt version %s on %s""" %
                (__version__, platform.python_version(), PySide.__version__,
                 PySide.QtCore.__version__, platform.system()))                        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())
