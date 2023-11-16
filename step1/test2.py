#-*- coding:utf-8 -*-
""" test2.py read Starred.tsv   convert col. 4 to Devanagari numbers.
"""
from __future__ import print_function
import sys, re,codecs

import transcoder
transcoder.transcoder_set_dir('transcoder')

def read_lines(filein):
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [x.rstrip('\r\n') for x in f]
 return lines

class Rec:
 def __init__(self,line):
  self.cols = line.split('\t')
  assert len(self.cols) == 19
  
def check_tabs(lines):
 title = None
 recs = []
 for iline,line in enumerate(lines):
  rec = Rec(line)
  if iline == 0:
   title = rec
  else:
   recs.append(rec)
 return title,recs

def transcode(x):
 tranin = 'slp1'
 tranout = 'deva'
 y = transcoder.transcoder_processString(x,tranin,tranout)
 return y

def adjust_recs(recs):
 # modify recs
 for rec in recs:
  # transcode 4th column
  col4 = rec.cols[3]
  col4_deva = transcode(col4)
  rec.cols[3] = col4_deva
  # remove column 2
  del rec.cols[1]

def adjust_title(titlerec):
  # remove column 2
  del titlerec.cols[1]
  # name for column 1
  titlerec.cols[0] = 'विशेषः'  # special
  
def recs_to_lines(titlerec,recs):
 # remove col 2 from titlerec
 outarr = []
 out = '\t'.join(titlerec.cols)
 outarr.append(out)
 for rec in recs:
  out = '\t'.join(rec.cols)
  outarr.append(out)
 return outarr

def write(fileout,outarr):
 with codecs.open(fileout,"w","utf-8") as f:
  for line in outarr:
   f.write(line + '\n')
 print(len(lines),"written to",fileout)

def check_cols(recs):
 # there is no title for last 3 cols
 # is this any data for these columns
 n = 0
 for irec,rec in enumerate(recs):
  cols = rec.cols
  cols1 = cols[-3:]
  cols1_str = ''.join(cols1)
  if cols1_str != '':
   irow = irec + 1
   print('row %s is not empty in last 3 columns' % irow)
   for j in (15,16,17):
    jrow = j + 1
    print(' col %s: %s' %(jrow,cols[j]))
   n = n + 1
 print(n,'instances where last 3 columns not empty')
 
def print_col_titles(titlerec):
 cols = titlerec.cols
 for icol,col in enumerate(cols):
  print('column %02d: %s' %(icol+1,cols[icol]))
  
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2]
 lines = read_lines(filein)
 titlerec,recs = check_tabs(lines)
 adjust_recs(recs)
 adjust_title(titlerec)
 # generate tsv text for titlerec and recs
 outarr = recs_to_lines(titlerec,recs)
 write(fileout,outarr)
 print_col_titles(titlerec)
 check_cols(recs)
 
