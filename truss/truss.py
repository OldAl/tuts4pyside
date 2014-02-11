#!/usr/bin/env python
# truss.py

# Copyright (c) 2010-2011, 2013 Algis Kabaila. All rights reserved.
# This work is made available under  the terms of the 
# Creative Commons Attribution-ShareAlike 3.0 license,
# http://creativecommons.org/licenses/by-sa/3.0/. 

import sys
import os
import platform

import PySide
from PySide.QtCore import QRect, QMetaObject, QObject
from PySide.QtGui  import (QApplication, QMainWindow, QWidget, 
                           QGridLayout, QTabWidget, QPlainTextEdit,
                           QMenuBar, QMenu, QStatusBar, QAction, 
                           QIcon, QFileDialog, QMessageBox, QFont)

import qrc_truss
import ncrunch

__version__ = '0.1.6'

class Truss(QMainWindow):
    def __init__(self, parent=None):
        super(Truss, self).__init__(parent)        
        self.resize(800, 600)
        self.filename  = None
        self.filetuple = None
        self.dirty = False  # Refers to Data Page only.
        centralwidget = QWidget(self)
        gridLayout = QGridLayout(centralwidget)
        self.tabWidget = QTabWidget(centralwidget)
        self.tab = QWidget()
        font = QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(12)
        self.tab.setFont(font)
        gridLayout_3 = QGridLayout(self.tab)
        self.plainTextEdit = QPlainTextEdit(self.tab)
        gridLayout_3.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setFont(font)
        gridLayout_2 = QGridLayout(self.tab_2)
        self.plainTextEdit_2 = QPlainTextEdit(self.tab_2)
        gridLayout_2.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.setCentralWidget(centralwidget)
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 800, 29))
        menu_File = QMenu(menubar)
        self.menu_Solve = QMenu(menubar)
        self.menu_Help = QMenu(menubar)
        self.setMenuBar(menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.action_New = QAction(self)
        self.actionSave_As = QAction(self)
        self.action_Save = QAction(self)
        self.action_Open = QAction(self)
        self.action_Quit = QAction(self)
        self.action_About = QAction(self)
        self.actionShow_CCPL = QAction(self)
        self.action_Solve = QAction(self)
        self.action_CCPL = QAction(self)
        self.action_Help = QAction(self)
        menu_File.addAction(self.action_New)
        menu_File.addAction(self.action_Open)
        menu_File.addAction(self.actionSave_As)
        menu_File.addAction(self.action_Save)
        menu_File.addSeparator()
        menu_File.addAction(self.action_Quit)
        self.menu_Solve.addAction(self.action_Solve)
        self.menu_Help.addAction(self.action_About)
        self.menu_Help.addAction(self.action_CCPL)
        self.menu_Help.addAction(self.action_Help)
        menubar.addAction(menu_File.menuAction())
        menubar.addAction(self.menu_Solve.menuAction())
        menubar.addAction(self.menu_Help.menuAction())        
        self.setWindowTitle("Main Window")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),\
                                   "Data Page")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),\
                                   "Solution Page")        
        menu_File.setTitle("&File")        
        self.menu_Solve.setTitle("&Solve")
        self.menu_Help.setTitle("&Help")
        self.tabWidget.setCurrentIndex(0)
        self.action_New.setText("&New") 
        self.action_Open.setText("&Open")       
        self.actionSave_As.setText("Save &As")
        self.action_Save.setText("&Save")
        self.action_Quit.setText("&Quit")        
        self.action_Solve.setText("&Solve")
        self.action_About.setText("&About")
        self.action_CCPL.setText("&CCPL")
        self.action_Help.setText("&Help")
        self.action_Quit.triggered.connect(self.close)
        allToolBar = self.addToolBar("AllToolBar") 
        allToolBar.setObjectName("AllToolBar") 
        self.addActions(allToolBar, (self.action_Open, self.actionSave_As,\
                        self.action_Save, self.action_Solve,\
                        self.action_Quit ))
        self.action_New.triggered.connect(self.fileNew)
        self.action_Open.triggered.connect(self.fileOpen)
        self.actionSave_As.triggered.connect(self.fileSaveAs)
        self.action_Save.triggered.connect(self.fileSave)
        self.action_Solve.triggered.connect(self.trussSolve)
        self.action_About.triggered.connect(self.aboutBox)
        self.action_CCPL.triggered.connect(self.displayCCPL)
        self.action_Help.triggered.connect(self.help)
        self.plainTextEdit.textChanged.connect(self.setDirty)
        self.action_New = self.editAction(self.action_New, None,\
                            'ctrl+N', 'filenew', 'New File.')   
        self.action_Open = self.editAction(self.action_Open, None, 
                            'ctrl+O', 'fileopen', 'Open File.')
        self.actionSave_As = self.editAction(self.actionSave_As,\
                            None, 'ctrl+A', 'filesaveas',\
                            'Save and Name File.')
        self.action_Save = self.editAction(self.action_Save, None, 
                            'ctrl+S', 'filesave', 'Save File.')
        self.action_Solve = self.editAction(self.action_Solve, None, 
                            'ctrl+L', 'solve', 'Solve Structure.')                                   
        self.action_About = self.editAction(self.action_About, None, 
                            'ctrl+B', 'about','Pop About Box.')                                  
        self.action_CCPL = self.editAction(self.action_CCPL, None, 
                            'ctrl+G', 'licence', 'Show Licence') 
        self.action_Help = self.editAction(self.action_Help, None, 
                            'ctrl+H', 'help', 'Show Help Page.')
        self.action_Quit =  self.editAction(self.action_Quit, None, 
                            'ctrl+Q', 'quit', 'Quit the program.')                                           
        self.plainTextEdit_2.setReadOnly(True)

    
    def setDirty(self):
        '''On change of text in textEdit window, set the flag
        "dirty" to True'''
        index = self.tabWidget.currentIndex()
        if index is not 0:
            return
        if self.dirty:
            return True
        self.dirty = True
        self.updateStatus('self.dirty set to True')    
    
    def clearDirty(self):
        'Clear dirty flag'
        self.dirty = False
    
    def fileNew(self):
        '''Clear both Data Page and Solution Page.'''
        self.plainTextEdit.setPlainText(' ')
        self.plainTextEdit_2.setPlainText(' ')
        self.clearDirty(self)

    def okToContinue(self):
        if self.dirty:
            reply = QMessageBox.question(self,
                    "Data Loader - Unsaved Changes",
                    "Save unsaved changes?",
                    QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Yes:
                self.clearDirty()
                return self.fileSave()
        return True
    
    def okRead(self):
        'Pop-up a warning message.'
        reply = QMessageBox.warning(self,
                "Warning",
                '''\nFile Open and Save is possible only in Data Page!
\n\(Use SaveAs for Solution Page)''', QMessageBox.Ok)
        return True

    def fileOpen(self):
        '''Open a file in Data Page (with index == 0)'''
        if self.tabWidget.currentIndex():
            self.okRead()
            return
        if not self.okToContinue():
            return
        dir = (os.path.dirname(self.filename)
               if self.filename is not None else ".")
        self.filetuple = QFileDialog.getOpenFileName(self,\
                        "Open File", dir, \
                        "Data (*.dat *.txt)\nAll Files (*.*)")
        self.filename = self.filetuple[0] 
        fname = self.filename        
#  QFileDialog returns a tuple x with x[0] = file name and 
#  x[1] = type of filter.
        if fname:
            self.loadFile(fname)
            self.filename = fname
            self.updateStatus('New file opened.')
                
    def loadFile(self, fname=None):
        fl = open(fname)
        text = fl.read()
        self.plainTextEdit.setPlainText(text)
        self.dirty = False
    
    def fileSave(self):
        '''Save file with current file name.'''
        if self.tabWidget.currentIndex():
            self.okRead()
            return        
        if self.filename is None:
            return self.fileSaveAs()
        else:
            flname = self.filename
            if flname:
                fl = open(flname, 'w')
                tempText = self.plainTextEdit.toPlainText()
                fl.write(tempText)
                fl.close()
                self.dirty = False
                self.updateStatus('File saved.')
                return True
            else:
                self.updateStatus('Failed to save... ')
                return False
        self.filename = None
        self.dirty = False

    def fileSaveAs(self):        
        '''Save file with a new name.'''
        qpr = self.qprintline
        fname = self.filename if self.filename is not None else\
        "NoName"
        self.filetuple = QFileDialog.getSaveFileName(self,
                "Truss program - Save File", fname, "Data File (*.*)")
        flname = self.filetuple[0]        
        index = self.tabWidget.currentIndex()
        if index == 0:
            self.filename = flname 
            if flname:
                fl = open(flname, 'w')
                tempText = self.plainTextEdit.toPlainText()
                fl.write(tempText)
                fl.close()
                self.dirty = False
                self.updateStatus('File saved.')   
        elif index == 1:
            if flname:
                fl = open(flname, 'w')
                tempText = self.plainTextEdit_2.toPlainText()
                fl.write(tempText)
                fl.close()


    def trussSolve(self):
        '''Solve a statically determinate truss, specified in
        Data Page and display the results in the Solution Page.
        To start, make a copy of the Data Page with a header all
        shown on the Data Page.'''
        printline = self.qprintline
        dataBall = self.plainTextEdit.toPlainText() 
        self.plainTextEdit_2.clear()
        printline('================================') 
        flbase = os.path.basename(self.filename)
        printline('SOLUTION FOR ' + flbase)
        printline('================================') 
        dataBall = self.plainTextEdit.toPlainText()
##       Diagnostic bit of code follows --------------
#        fo = open('dataBallFile', 'w')
#        fo.write(dataBall)
#        fo.close
##       Diagnostic end                 --------------
        ncrunch.main(printline, self.filename, dataBall)

    def aboutBox(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PySide, Platform and the like",
                """<b>Part of Structural Analysis.</b> v %s
                <p>Copyright &copy; 2011 Algis Kabaila. 
                All rights reserved in accordance with
                Creative Commons Attribution Licence (CCPL) v3
                or later - NO WARRANTIES!
                <p>This progam finds bar forces in 
                statically determinate trusses.                
                <p>Python %s -  PySide version %s - Qt version %s on\
                %s""" % (__version__, platform.python_version(),\
                PySide.__version__,  PySide.QtCore.__version__,
                platform.system()))
              
    def displayCCPL(self):
        '''Read and display CCPL licence.'''
        self.plainTextEdit.setPlainText(open('CCPL.txt').read())
        self.dirty = False
        self.filename = 'COPYING.txt'
        self.updateStatus('CCPL displayed.')

    def help(self):
        '''Read and display a help file- currently the README.txt.'''
        self.plainTextEdit.setPlainText(open('README.md').read())
        self.dirty = False
        self.filename = 'README.txt'
        self.updateStatus('README displayed.')
        
    def addActions(self, target, actions):
        '''Actions are added to Tool Bar.'''
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
    
    def editAction(self, action, slot=None, shortcut=None, icon=None,
                     tip=None):
        '''This method adds to action: icon, shortcut, ToolTip,\
        StatusTip and can connect triggered action to slot '''
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % (icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)                        
        return action

    def qreadline(self, lineNo):
        '''Read one line from Data Page (lineNo starts with 0)'''
        return unicode(self.plainTextEdit.document().\
            findBlockByLineNumber(lineNo).text()).rstrip()

    def qprintline(self, line):        
        '''Append one line to Solution Page.'''
        self.plainTextEdit_2.appendPlainText(line.rstrip())

    def updateStatus(self, message):
        '''Keep status current.'''
        if self.filename is not None:
            flbase = os.path.basename(self.filename)
            self.setWindowTitle(unicode("Truss Analysis - " +\
                                         flbase + "[*]") )
            self.statusBar().showMessage(message, 5000)
            self.setWindowModified(self.dirty)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Truss()
    frame.show()
    sys.exit(app.exec_())
    
# ----------------------------------------------------------------------
# 0.0.0 Pattern 2010-12-28
# 0.0.1 eliminated truss.ui 2010-12-28
# 0.0.2 commented out setObjectName statements 2011-01-06.
# 0.0.3 added menu entry for action About 2011-01-06.
# 0.0.4 addec actions to tool bar, no icons 2011-01-06.
# 0.0.5 all menu and tool bar actions debug-working, no icons 2011-01-06
# 0.0.6 icons added, debug working stage GUI ok 2011-01-06
# 0.0.7 made same variables local in proc __init__ 2011-01-08
# 0.0.8 add Policy. Testing qreadline, qprintline 2011-01-09
# 0.0.9 most methods of GUI ok.  2011-01-13 
# 0.1.0 GUI is finished, though not debugged. 2011-01-14
# 0.1.1 Copy data with a heading as output - 1st step. 2011-01-15
# 0.1.2 Fully working program just before wrecking 
#       it with 'structure'. Wrecking postponed. 2011-01-19
# 0.1.3 All done 4 examples. "Crunch is broken to methods. 2011-01-21
# 0.1.4 Basic Matrix module (basemat) simplified. 2011-01-21
# 0.1.5 Matrix module "retired", re-arranged all code. 2011-02-07
# 0.1.6 References to GPL replaced by CCPL.  2014-02-11    

# Complex trusses - ref. A. Hall and A. Kabaila, "Basic Concepts of
# Structural Analyis", Pitman, UK ISBN 0 273 01108 1
# Titles not displayed for help and show GPL - set self.filename!
    
