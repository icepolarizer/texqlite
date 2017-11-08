#-*- coding:utf-8 -*-
import sys, os
reload(sys)
sys.setdefaultencoding('utf8')

import sqlite3

help_manual = """
This is a program which converts text file to sqlite db.\n
Usage example: txt-sqlite.py -i
"""

"""
arg = sys.argv

for i in arg:
    if i == '-o': output_filename = arg[arg.index(i)+1]
    elif i == '-f': input_filename = arg[arg.index(i)+1]
    elif i == '-s': separator = arg[arg.index(i)+1]
    elif i == '-is': inner_sepa = arg[arg.index(i)+1]
    elif i == '-tbn': table_name = arg[arg.index(i)+1]


if output_filename == None: output_filename = 'sqlite_converted.db'
"""
if '-i' in sys.argv:
    input_filename = raw_input("Input filename: ")
    output_filename = raw_input("Output filename: ")
    separator = raw_input("Record separator string: ")
    inner_sepa = raw_input("Field separator string: ")
    table_name = raw_input("Table name: ")
    fields = raw_input("Fields(example: field1 text, field2 text): ")
else:
    input_filename = sys.argv[1]
    output_filename = 'output.db'
    separator = ','
    inner_sepa = None
    fields = "Field1 text"
    table_name = input_filename.split('.')[0]


f = open(input_filename)
txtdb = f.read()
f.close()

txtdb_table = txtdb.split(separator)

conn = sqlite3.connect(output_filename)
curs = conn.cursor()

print 'CREATE TABLE %s (%s)' % (table_name, fields)

curs.execute('CREATE TABLE %s (%s)' % (table_name, fields))
sqlite_values = []

if inner_sepa == None:
    print 'inner sepa is none!'
    for j in txtdb_table:
        sqlite_values.append((j,))
else:
    for j in txtdb_table:
        sqlite_values.append((tuple(j.split(inner_sepa))))

print sqlite_values

print 'insert into %s values(%s)' % (table_name, ('?,'*len(fields.split(',')))[:-1])

curs.executemany(
        'insert into %s values(%s)' % (table_name, ('?,'*len(fields.split(',')))[:-1]), sqlite_values
        )
conn.commit()
conn.close()
