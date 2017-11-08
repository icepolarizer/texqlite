import sqlite3
conn = sqlite3.connect('posts.db')
curs = conn.cursor()
post_values = [(session['username'], post_title, post_content),]
curs.executemany('insert into posts values(?,?,?)', post_values)
conn.commit()
conn.close()
