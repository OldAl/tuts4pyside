readme.md for **icons**
==========================

The **combine.qrc** is prepared with a plane text editor, such as **kate** or **vim** (not a word processor, such as libre office writer or MS Word).  It is a XML file which is easily written following the extant pattern.

Inspection of the file reveals the replacement of the path to the icon by much simpler token. In application, it is called by a simple token and a special format - see later.

In a similar way to the file in **qt-designer**, the XML file needs to be converted to a python readable file, with a pyside compile **pyside-rcc**:

pyside-rcc combine.qrc -o <output file>

We choose a name for the output file which indicates that it is

* a python file, so it has an extension py
* a user interface data file, so it has a prefix qrc_

Thus, the command is **pyside-rcc combine.qrc -o grc_combine.py**. 

qrc_combine.py should then be copied to other directories as required.
