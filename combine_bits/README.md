
README.md for *combine_bits* section
=====================================

### Introduction

Returning to this work after an interruption of several months, I thought this section looked like a proverbial **dog's breakfast**, so I shall re-organise it. 

### Thank you

My sincere gratitude to **Aaron Richiger**, a guru of PySide who made some valuable suggestions, without ever discouraging. The errors and inadequacies are all mine and mine alone. 

### Sequence

1.  combine-STAGE1.py
2.  combine.py
3.  combine_allin1.py
4.  combine_alter.py

### Separation into subdirectories

The information shared by each of the methods of combining the three parts of the program (**about_box, quit_prog and show_licence**) are in two directories: **designer** and **icons**. The combine.py, combine_alter.py  and the combine_allin1.py will require the data from **designer** and **icons** directories.  The readme.md in each of these two directories briefly describe what is to be done in each of these.

So the directoy structure of **combine_bits** has the following subdirectories:

* icons
* designer
* combine_folder
* combine_alter_folder
* combine_allin1_folder

### *combine_folder* directory.

In this directory are the following main programs:
 
* **combine-STAGE1.py**
* **combine.py**

**STAGE1** is a fully functional program, but it lacks icons and some other "trimmings"; **combine.py** has icons etc. 
It is the 'finished product', as far as this tutorial is concerned. If you wish to skip the rest of this tutorial, this may be the right place for it.

Other versions of this program are there two show different ways to achieve the same objectives.

### *combine_alter_folder* directory

Another popular way of proceeding, which avoids the use of double inheritance.

### *combine_allin1_folder* directory

A program that avoids qt-designer created files. For the fearless. I cheated by copying parts of the qt-designer made files.

Al Kabaila, 2014-01-09

