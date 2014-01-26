readme.md for **icons**
==========================

The **combine.qrc** is prepared with a plain text editor, such as **kate** or **vim** (not a word processor, such as libre office writer or MS Word).  It is a XML file which is easily written following the extant pattern.

Inspection of the file reveals the replacement of the path to the icon by a much simpler token. Applications refer to icons by that token. For the format, find the token name in the code.

In a similar way to the file in **qt-designer**, the XML file needs to be converted to a python readable file, with a pyside compiler **pyside-rcc**:

* **pyside-rcc [options] combine.qrc -o <output file>**

One of the options is to produce the <output file> for python3; the default is python2.
The switch for python3  is **-py3**, so that the above command for 
python3 becomes:

* **pyside-rcc -py3 combine.qrc -o <output file>**

We choose a name for the output file which indicates that it is

* a python file, so it has an extension py
* a user interface data file, so it has a prefix qrc_
* main part of the name is **combine**, which identifies the project.
* indication of python version - 2 for python 2.x, 3 for python 3.x
* Thus, the command for python2.x is **pyside-rcc combine.qrc -o qrc_combine2.py**
* For pyhthon3.x the command is **pyside-rcc -py3 combine.qrc -o qrc_combine3.py**. 

**qrc_combinex.py** should then be copied to other directories as required.


