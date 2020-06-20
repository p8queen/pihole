import sqlite3

db = sqlite3.connect('gravity.db')
cur = db.cursor()

with open('regex.list','r') as f:
    domains = f.read().splitlines()

for c in domains:
    if len(c)>3:
        d = (3,'*'+c+'*')
        sql = """INSERT INTO domainlist(type,domain) VALUES(?,?)"""
        cur.execute(sql,d)
        db.commit()

cur.close()
print('--end---')



