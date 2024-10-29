import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL            
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
users_data = []
for i in range(10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)', (f"User{i+1}",f"example{i+1}@gmail.com",f"{i+1}*10",f"1000"))
    users_data.append(i)

for j in range(1, len(users_data), 2):
    cursor.execute('UPDATE Users SET balance = balance - 500 WHERE id = ?', (j + 1,))

for k in range(0, len(users_data), 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (k + 1,))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
results = cursor.fetchall()

for user in results:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute("SELECT COUNT(*) FROM Users")
total1 = cursor.fetchone()[0]
print(total1)

cursor.execute("SELECT SUM(balance) FROM Users")
total2 = cursor.fetchone()[0]
print(total2)

cursor.execute("SELECT AVG(balance) FROM Users")
total3 = cursor.fetchone()[0]
print(total3)

connection.commit()
connection.close()