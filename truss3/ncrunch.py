#!/usr/bin/env python3
# ncrunch.py revised number cruncher module

# Copyright (c) 2010-2011, 2013 Algis Kabaila. All rights reserved.
# This work is made available under  the terms of the 
# Creative Commons Attribution-ShareAlike 3.0 license,
# http://creativecommons.org/licenses/by-sa/3.0/. 

import sys

import io
import math

import numpy as np
from numpy import linalg as la

# Global functions

def printerm(printline, a, LineLen=5):
    ''' Output (Matrix a, [Line length]) -> Output matrix a of size (m x n)
    according to function printline. Line length can be specified as 3-rd parameter.'''
    m, n = len(a), len(a[0])
    printline('Matrix of dimensions' + ' (%s x %s)' % (m, n)) 
    for i in range(m):
        line = ''
        for j in range(n):
            line += (' %12.5E ' % a[i, j])
            if ( (j + 1) % LineLen) == 0:
                printline(line) # New line
                line = ''
        printline(line)
        # blank line between rows if len(row) > 5 
        if (j == (n - 1)) and ((j + 1) > LineLen) :
            printline(' ')
    return


def printdict(printline, a):
    '''Print dictionary "a" in almost decent format.'''
    keys = list(a.keys())
    keys.sort()
    for i in keys:
        printline(str(i) + ' ' + a[i].__str__())
    
class Cruncher():
    def __init__(self, name, printline, dataBall):
        '''Receive arguments and store as class variables.'''
        self.name   = name
        self.printline = printline
#        self.dataBall = dataBall
        self.fin = io.StringIO(dataBall)  # Open for reading
     
    def lineread(self):
        '''Read and echo a line. Only return line without "#" character,'''
        while True:
            # read line - loop for ever
            line = self.fin.readline()
            # echo line
            self.printline(line)       
            if not ('#' in line):
                break
        return line       
   
    def prolog(self):       
        fin = self.fin
        lineread = self.lineread
        printline = self.printline
        for line in fin:
            printline(line.strip())
        fin.seek(0, 0)  # rewind file
        printline('*** Data Echo Finished ***')
        printline('echo of "general" flag.')
        lineread()
        lst = lineread().split()
        assert lst[0] == "g", 'First Charactero should be == "g"'
        noNodes = int(lst[1])
        noMembers = int(lst[2])
        noAuxiliaries = int(lst[3])
        noLoadCases = 1
        lst = lineread().split()
        assert lst[0] == "g", 'First Charactero should be == "g"'        
        noLoadLines = int(lst[1])  # do it for one Load Case only.
        printline("noLoadLines = " + str(noLoadLines))
        return lineread, noNodes, noMembers, noAuxiliaries,\
        noLoadCases, noLoadLines
    
    def doNodes(self, lineread, noNodes, noAuxiliaries):
        flag = lineread()
        assert flag.strip() == 'nodes', '"nodes" signals that nodal data follows'
        nodes = {}
        for i in range(noNodes + noAuxiliaries):
            lst = lineread().split()
            assert lst[0] == 't', 'Data for ordinary nodes starts with "t".'
            nodeNo = int(lst[1])
            x_coord = float(lst[2])
            y_coord = float(lst[3])
            freedom_x = (nodeNo - 1) * 2 + 1
            freedom_y = freedom_x + 1
            nodes[nodeNo] = (nodeNo, x_coord, y_coord, freedom_x, freedom_y)
            self.printline('Node freedoms %s %s  ' % (str(freedom_x), str(freedom_y)))
        return nodes
    
    def doMembers(self, lineread, noMembers, noAuxiliaries):
        flag = lineread()    
        assert flag.strip() == 'members', '"members" flag start of member data'
        members = {}
        for i in range(noMembers + noAuxiliaries):
            lst = lineread().split()
            assert lst[0] == 't', 'Truss member data starts with "t"'
            no = int(lst[1])
            end1 = int(lst[2])
            end2 = int(lst[3])
            members[no] = (no, end1, end2)
        return members
    
    def doMemprops(self, noMembers, noAuxiliaries,\
                    members, nodes):
        '''Calculate and store directory of 
        Member Properties.'''
        printline = self.printline
        memprops = {}
        for i in range(noMembers + noAuxiliaries):
            member = members[i+1]
            printline(member.__str__())
            # end1, end2 = end node nos
            end1 = member[1]
            end2 = member[2]
            locvec = [nodes[end1][3], nodes[end1][4], nodes[end2][3],\
                       nodes[end2][4]]
            dx = nodes[end2][1] - nodes[end1][1]
            dy = nodes[end2][2] - nodes[end1][2]
            memlen = math.sqrt(dx * dx + dy * dy)
            cosx = dx / memlen
            cosy = dy / memlen
            dircos = [cosx, cosy]
            memprops[i + 1] = locvec + dircos
            z = locvec
            printline('member_no, locvec = %s   %s %s %s %s ' %\
                       (str(i + 1), str(z[0]), str(z[1]), str(z[2]), str(z[3])))
            printline('direction cosines = %s %s ' % (str(cosx), str(cosy)))                                                
        return memprops

    def crunch(self):
        '''Mainline to number crunch the calculation of
        member foreces.'''
# echo data:
        printline = self.printline
        lineread, noNodes, noMembers, noAuxiliaries,\
        noLoadCases, noLoadLines = self.prolog()
        nodes = self.doNodes(lineread, noNodes, noAuxiliaries)       
        printline("nodes = ")
        printdict(printline, nodes)
        members = self.doMembers(lineread, noMembers, noAuxiliaries)       
        printline('members = ') 
        printdict(printline, members)    
        memprops = self.doMemprops( noMembers, noAuxiliaries, members, nodes)
        printline('memprops =')
        printdict(self.printline, memprops)
        ndim = noNodes * 2
        printline('Dimension of connection mat ndim =' + str(ndim))
        connection = np.zeros((ndim, ndim), dtype = "float")
        for i in range(noMembers + noAuxiliaries):
            member = memprops[i + 1]
            connection[member[0] - 1, i] += member[4]
            connection[member[1] - 1, i] += member[5]
            if i < noMembers:                
                connection[member[2] - 1, i] += -member[4]            
                connection[member[3] - 1, i] += -member[5]
        printline(' ')
        printline('Connection matrix')
        printerm(printline, connection)
        try:
            conditionnumber = la.cond(connection)
            inv = la.inv(connection)
        except la.LinAlgError as e:
            printline( '%s  %s' % (type(e).__name__, e))
        else:
            i = np.dot(inv, connection)
            loads = np.zeros((ndim, 1), dtype = "float")   
            line = lineread()
            assert line.strip() == 'loads', 'Flag for loads is loads'
            for i in range(noLoadLines):
                lst = lineread().split()
                nodeNo = int(lst[0])
                node = nodes[nodeNo]
                loads[node[3] - 1] = -float(lst[1])
                loads[node[4] - 1] = -float(lst[2])
            printline('')
            printline('Load matrix = ')
            printerm(printline, loads)
            memberActions = np.dot(inv, loads)
            printline(' ')
            printline("Member Actions, [Ni | Ri] matrix.")
            printerm(printline, memberActions)
        printline(' ')
        printline('matrix condition number = ' + str(conditionnumber))
        printline(' ')

def main(printline, name, dataBall):
    cruncher = Cruncher(name, printline, dataBall)
    cruncher.crunch()
    
if __name__ == '__main__':
    
    def printline(line):
        print(line)    
    print('Usage: Give a name for data in the "dat" subdirectory')
    print('as program parameter. Default is "sdtruss1.dat"')
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = 'sdtruss1.dat'
    try:
        with open('dat/' + name, 'r') as finput:
            dataBall = str(finput.read())       
    except IOError:
        print('Failed to open given file name.')
        sys.exit(1)
    main(printline, name, dataBall)
    
