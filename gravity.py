import sqlite3

db = sqlite3.connect('gravity.db')
cur = db.cursor()

with open('regex.list','r') as f:
    domains = f.read().splitlines()

for c in domains:
    d = '*'+c+'*'
    if len(d)>3: print(d)

print('--end---')



