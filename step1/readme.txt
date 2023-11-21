step1  
Numbering-Skt-Final-15thNov23Starred.tsv  from Usha.

---------------------------------------------------------------

python test1.py Numbering-Skt-Final-15thNov23Starred.tsv test1.txt

Each line has 19 columns. Great!
first line is a 'title' line
---------------------------------------------------------------

a. Transcode column 4 to Devanagari (the 'number' for this row)
   not for row 1
b. Remove column 2  (duplicate 'number' column) -- unneeded

python test2.py  Numbering-Skt-Final-15thNov23Starred.tsv test2.txt

Column titles
column 01: विशेषः
column 02: आङ्ग्ले
column 03: संस्कृते
column 04: सङ्ख्या (प्रातिपदिकम्)
column 05: पुंलिङ्गम्
column 06: स्त्रीलिङ्गम्
column 07: नपुंसकलिङ्गम्
column 08: सङ्ख्यानम् (प्रातिपदिकम्)
column 09: सङ्ख्यानम् (पुंलिङ्गम्)
column 10: सङ्ख्यानम् (स्त्रीलिङ्गम्)
column 11: सङ्ख्यानम् (नपुंसकलिङ्गम्)
column 12: सङ्ख्यानम्-तम (प्रातिपदिकम्)
column 13: सङ्ख्यानम्-तम (पुंलिङ्गम्)
column 14: सङ्ख्यानम्-तम (स्त्रीलिङ्गम्)
column 15: सङ्ख्यानम्-तम (नपुंसकलिङ्गम्)
column 16:
column 17:
column 18:

Are columns 16-18 always empty? No
row 1 is not empty in last 3 columns
 col 16: రెండు
 col 17: రెండవ
 col 18: రెండు
row 2 is not empty in last 3 columns
 col 16: एक
 col 17: पहला
 col 18:
row 3 is not empty in last 3 columns
 col 16: दो
 col 17: दूसरा
 col 18:
row 4 is not empty in last 3 columns
 col 16: तीन
 col 17: तीसरा
 col 18:

---------------------------------------------------------------
11-20-2023
Revision of test2.txt (manually on Github)
  (remove some asterisks)
git pull
-----
cp test2.txt tempprev_test2.txt

Comparable revision of Numbering-Skt-Final-15thNov23Starred.tsv (local)

Rerun construction of test2.txt
python test2.py  Numbering-Skt-Final-15thNov23Starred.tsv test2.txt
Now the calculated test2.txt has the revisions
  So git status yields only changes to Numberin...txt and readme.txt.
