import sqlite3

# just creates our database
def create_db():
    conn = sqlite3.connect("posting.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posting (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

# executes our query and returns the results
def query_db(query):
    db = sqlite3.connect("posting.db")
    cursor = db.execute(query)
    records = cursor.fetchall()
    cursor.close()
    db.commit()
    db.close()
    return records

if __name__=="__main__":
    create_db()