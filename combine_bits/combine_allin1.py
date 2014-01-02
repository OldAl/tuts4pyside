#!/usr/bin/env python3

# Copyright (c) 2010-2011, 2013 Algis Kabaila. All rights reserved.
# This work is made available under  the terms of the 
# Creative Commons Attribution-ShareAlike 3.0 license,
# http://creativecommons.org/licenses/by-sa/3.0/. 

# combine.py - combination of ShowGPL, About, Close scripts   
# The purpose of this version of program is to show implementation
# of most code in one file - all_in_1!. The Ui_MainWindow is eliminated
# and does not appear in the program.
     
import sys
import platform
     
import PySide
     
from PySide.QtCore import QRect
from PySide.QtGui import (QApplication, QMainWindow, QMessageBox,
                          QIcon, QAction, QWidget, QGridLayout,
                          QTextEdit, QMenuBar, QMenu, QStatusBar)
     
__version__ = '3.0.0'

import qrc_combine
     
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(730, 475)
        self.setWindowTitle('Combine Code Blocks.')
        centralwidget = QWidget(self)
        gridLayout = QGridLayout(centralwidget)
        # textEdit needs to be a class variable.
        self.textEdit = QTextEdit(centralwidget)
        gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.setCentralWidget(centralwidget)
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 731, 29))
        menu_File = QMenu(menubar)
        self.setMenuBar(menubar)
        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)
        actionShow_GPL = QAction(self)
        actionShow_GPL.triggered.connect(self.showGPL)
        action_About = QAction(self)
        action_About.triggered.connect(self.about)        
        iconToolBar = self.addToolBar("iconBar.png")
#------------------------------------------------------
# Add icons to appear in tool bar - step 1
        actionShow_GPL.setIcon(QIcon(":/showgpl.png"))
        action_About.setIcon(QIcon(":/about.png"))
        action_Close = QAction(self)
        action_Close.setCheckable(False)
        action_Close.setObjectName("action_Close")        
        action_Close.setIcon(QIcon(":/quit.png"))
#------------------------------------------------------
# Show a tip on the Status Bar - step 2
        actionShow_GPL.setStatusTip("Show CC Licence")
        action_About.setStatusTip("Pop up the About dialog.")
        action_Close.setStatusTip("Close the program.")
#------------------------------------------------------
        menu_File.addAction(actionShow_GPL)
        menu_File.addAction(action_About)
        menu_File.addAction(action_Close)
        menubar.addAction(menu_File.menuAction())
     
        iconToolBar.addAction(actionShow_GPL)
        iconToolBar.addAction(action_About)
        iconToolBar.addAction(action_Close)
        action_Close.triggered.connect(self.close)
                 
    def showGPL(self):
        '''Read and display CCPL licence.'''
        with open('CCPL.txt') as nonamefile:
            self.textEdit.setText(nonamefile.read())               
           
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
