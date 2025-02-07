import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books
          (title TEXT, pages INTEGER)''')

c.execute('''INSERT INTO books VALUES("Are You My Mother?", 72)''')
conn.commit()

books = [
    ("Are You My Mother?", 72),
    ("The Digging-est Dog", 72),
    ("The Giving Tree", 68)
]
c.executemany('''INSERT INTO books VALUES(?, ?)''', books)
conn.commit()

c.execute('''SELECT rowid, title FROM books''')
data = c.fetchall()
print(data)

# c.execute('''DELETE FROM books WHERE rowid=2''')
# conn.commit()

c.execute('''UPDATE books SET title="Crash Proof" WHERE rowid=2''')
conn.commit()

c.execute('''SELECT * FROM books''')
data = c.fetchall()
print(data)