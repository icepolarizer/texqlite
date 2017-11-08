#-*- coding:utf-8 -*-
import sys, os
reload(sys)
sys.setdefaultencoding('utf8')

import sqlite3

help_manual = """
This is a program which converts text file to sqlite db.\n
Usage example: txt-sqlite.py -f textfile.txt -o sqlite_output.db -s , -is --
"""

arg = sys.argv

for i in arg:
    if i == '-o': output_filename = arg[arg.index(i)+1]
    elif i == '-f': input_filename = arg[arg.index(i)+1]
    elif i == '-s': separator = arg[arg.index(i)+1]
    elif i == '-is': inner_sepa = arg[arg.index(i)+1]

if output_filename == None: output_filename = 'sqlite_converted.db'

f = open(input_filename)
txtdb = f.read()
f.close()

txtdb_table = txtdb.split(separator)

conn = sqlite3.connect(output_filename)
curs = conn.cursor()
sqlite_values = []

for j in txtdb_table:
    sqlite_values.append((tuple(j.split(inner_sepa))))

curs.executemany(
        'insert into posts values(%s)' % '?,'*len(sqlite_values[0]), post_values
        )
conn.commit()
conn.close()
