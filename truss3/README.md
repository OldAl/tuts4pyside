##README.md for section called **truss3**

### truss3 directory

This directory is a copy of truss directory, modified for Python3.
It aims to be the same as the program in the truss directory, but to run
under python 3.x. It is assumed that **python3** points to the currently
installed Python 3.x program. At the time of writing Python 3.x is Python 3.2.
Please notice that truss.py and ncrunch.py are somewhat different in truss 
directory and in truss3 directory. In other words, they are not interchangeable.

### Operating Truss programs

The truss program can be run as a CLI program without a gui as follows:

*    python3 ncrunch.py [input file name from dat directory] > [output file name]

For example, to check out sdtruss2, we can find the data for that truss in
dat/sdtruss2.dat. So to get the output in the current directory, do the following:

*    python3 ncrunch.py  sdtruss2.dat > sdtruss2.out

To run the program with GUI, enter the following line of code

*    python3 truss.py

or for file manager, such as Dolphin, double click the truss.py file.    

### Basic Help

The data is created in the Data Page. Alternatively it can be read from a file
into the Data Page.  When required it is modified, but only in the Data Page. It 
is advisable to save the Data Page before beginning any analysis.

The analysis results are stored by the program in the Solution Page.  Some errors
in data may cause the program to fail without necessarily displaying any 
information on the Solution Page.

The Solution Page is read only, though it can be saved into a file - with the 
SaveAs option.

Unlike command line programs, there are no restrictions where the data is stored, nor any restrictions where the results are stored. It is recommended to use *.dat format* for the data files and the *.out format* for output files. For consistency, all data files are stored in the ./dat subdirectory and all output files are stored in ./out subdirectory.

It is advisable to be systematic wrt to the above aspect.  All the examples 
should be stored always in the same directory and all the answers of the 
standard examples will be stored in another directory which should remain the same relative to the main program.

These notes are simply a part of the program, as much as the data for standard 
examples.  You are free and encouraged to change this help and extend this help 
page,

ak 2011-01-14
