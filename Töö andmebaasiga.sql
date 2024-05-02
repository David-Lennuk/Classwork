from sqlite3 import connect, Error
from os.path import abspath, dirname, join
from datetime import datetime

def create_connection(path: str):
    connection = None
    try:
        connection = connect(path)
        print("Ühendus on olemas!")
    except Error as e:
        print(f"Tekkis viga: {e}")
    return connection

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Päring õnnestus.")
    except Error as e:
        print(f"Tekkis viga: {e}")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Tekkis viga: {e}")

def execute_insert_query(connection, data):
    query = "INSERT INTO users(Name, Lname, Age, Residence, Birthday, GenderId) VALUES(?,?,?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

filename = abspath(__file__)
dbdir = dirname(filename)
dbpath = join(dbdir, "data.db")

create_gender_table = """
CREATE TABLE IF NOT EXISTS gender (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nimetus TEXT NOT NULL
);
"""

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Lname TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Residence TEXT NOT NULL,
    Birthday TEXT NOT NULL,
    GenderId INTEGER,
    FOREIGN KEY (GenderId) REFERENCES gender (Id)
);
"""

insert_gender = "INSERT INTO gender(Nimetus) VALUES('mees'),('naine');"

insert_users = """
INSERT INTO users(Name, Lname, Age, Residence, Birthday, GenderId)
VALUES
    ("David", "Lennuk", 17, "Tallinn", '2007-04-01', 1),
    ("Mark", "Nikolajev", 25, "Tallinn", '1998-06-05', 1),
    ("Alina", "Cvetkova", 39, "Tallinn", '1985-09-10', 2),
    ("Igor", "Aster", 33, "Tallinn", '1980-05-10', 1),
    ("Timur", "Basirov", 19, "Tallinn", '2005-01-15', 1);
"""

select_users = "SELECT * FROM users"
select_users_gender = """
SELECT users.Name, users.Lname, gender.Nimetus 
FROM users 
INNER JOIN gender ON users.GenderId = gender.Id
"""

conn = create_connection(dbpath)
execute_query(conn, create_gender_table)
execute_query(conn, insert_gender)
execute_query(conn, create_users_table)
execute_query(conn, insert_users)

insert_user = (
    input("Eesnimi: "),
    input("Perenimi: "),
    int(input("Vanus: ")),
    input("Elukoht: "),
    datetime.strptime(input("Sisestage sünnikuupäev (YYYY-MM-DD): "), "%Y-%m-%d").date(),
    int(input("Sugu (1 - mees, 2 - naine): "))
)
execute_insert_query(conn, insert_user)

users = execute_read_query(conn, select_users)
print("Kasutajate tabel:")
for user in users:
    print(user)

genders = execute_read_query(conn, select_users_gender)
print("Kasutajate tabel koos sooga:")
for gender in genders:
    print(gender)
