import sqlite3

# Step 1: Connect to the database (creates file if not exists)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Step 2: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Step 3: Insert data into the table
users_to_insert = [
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com')
]

cursor.executemany('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', users_to_insert)

# Step 4: Fetch and display data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("Users in the database:")
for row in rows:
    print(row)

# Step 5: Commit and close connection
conn.commit()
conn.close()
