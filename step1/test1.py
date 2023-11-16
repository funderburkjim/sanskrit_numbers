#-*- coding:utf-8 -*-
""" read Starred.tsv
"""
from __future__ import print_function
import sys, re,codecs

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

def check_tabs(lines):
 outarr = []
 # title line
 for iline,line in enumerate(lines):
  lnum = iline + 1
  parts = line.split('\t')
  nparts = len(parts)
  outarr.append('line %s %s columns: %s' %(lnum,nparts,line))
 return outarr

def write(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in outarr:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2]
 lines = read_lines(filein)
 outarr = check_tabs(lines)
 write(fileout,outarr)
 
