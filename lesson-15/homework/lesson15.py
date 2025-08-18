import sqlite3

# 1. Создать (или подключиться к) базе данных
conn = sqlite3.connect('startrek.db')
cursor = conn.cursor()

# 2. Создать таблицу Roster
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# 3. Вставить данные
cursor.executemany('''
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

conn.commit()

# 4. Обновить имя Jadzia Dax на Ezri Dax
cursor.execute('''
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
''')
conn.commit()

# 5. Вывести имя и возраст всех Bajoran
cursor.execute('''
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran'
''')

rows = cursor.fetchall()
print("Bajoran characters:")
for name, age in rows:
    print(f"Name: {name}, Age: {age}")

# 6. Закрыть соединение
conn.close()
