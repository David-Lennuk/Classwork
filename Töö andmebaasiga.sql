#from sqlite3 import *
#from sqlite3 import Error
#from os import *

#def create_connect(path:str):
#    connection=None
#    try:
#        connection=connect(path)
#        print("Ühendus on olemas!")
#    except Error as e:
#        print(f"Tekkis viga: {e}")
#    return connection
#def execute_query(connection,query):
#    try:
#        cursor=connection.cursor()
#        cursor.execute(query)
#        connection.commit()
#        print("Tabel on loodud või andmed on sisestatud")
#    except Error as e:
#        print(f"Tekkis viga: {e}")
#def execute_read_query(connection,query):
#    cursor=connection.cursor()
#    result=None
#    try:
#        cursor.execute(query)
#        result=cursor.fetchall()
#        return result
#    except Error as e:
#        print(f"Tekkis viga: {e}")
#def execute_insert_query(connection,data):
#    query="INSERT INTO users(Name,Lname,Age,GenderId) VALUES(?,?,?,?)"
#    cursor=connection.cursor()
#    cursor.execute(query,data)
#    connection.commit()

#def dropTable(connection, table):
#    try:
#        cursor = connection.cursor() 
#        cursor.execute(f"DROP TABLE IF EXISTS {table}")
#        connection.commit() 
#        #print("Table on kustutatud)
#    except Error as e:
#        print(f"Tekkis viga: {e}")
        

#create_users_table = """
#CREATE TABLE IF NOT EXISTS users(
#id INTEGER PRIMARY KEY AUTOINCREMENT,
#Name TEXT NOT NULL,
#Lname TEXT NOT NULL,
#Age INTEGER NOT NULL,
#Residence  TEXT NOT NULL,
#Birthday DATETIME NOT NULL,
#GenderId INTEGER,
#FOREIGN KEY (GenderId) REFERENCES gender (Id)
#)
#"""

#insert_users = """
#INSERT INTO users(Name,Lname,Age,Residence,Birthday,Gender)
#VALUES
#("David", "Lennuk", 17, "Tallinn", '2007-04-01', "Man"),
#("Mark", "Nikolajev", 25, "Tallinn", '1998-06-05', "Man"),
#("Alina", "Cvetkova",39, "Tallinn", '1985-09-10', "Women"),
#("Igor", "Aster",33, "Tallinn", '1980-05-10', "Man"),
#("Timur", "Basirov",19, "Tallinn", '2005-01-15', "Man")
#"""

#insert_gender="INSERT INTO gender(Nimetus) VALUES('mees'),('naine')"
#select_users="SELECT * from users"
#select_users_gender="SELECT users.Name,users.Lname,gender.Nimetus from users INNER JOIN gender ON users.GenderId=gender.Id"

#create_gender_table="CREATE TABLE IF NOT EXISTS gender(Id INTEGER PRIMARY KEY AUTOINCREMENT,Nimetus TEXT NOT NULL)"
#insert_users="""
#INSERT INTO
#users(GenderId)
#VALUES
#(1),
#(1),
#(2),
#(1)
#(1)
#"""
#insert_gender="INSERT INTO gender(Nimetus) VALUES('mees'),('naine')"
#select_users="SELECT * from users"
#select_users_gender="SELECT users.Name,users.Lname,gender.Nimetus from users INNER JOIN gender ON users.GenderId=gender.Id"


#select_users = "SELECT * FROM users"
#insert_gender="INSERT INTO gender(Nimetus) VALUES('mees'),('naine')"
#select_users="SELECT * from users"
#select_users_gender="SELECT users.Name,users.Lname,gender.Nimetus from users INNER JOIN gender ON users.GenderId=gender.Id"


#filename=path.abspath(__file__)
#dbdir=filename.rstrip('Too_andmebaasiga.py')
#dbpath=path.join(dbdir,"data.db")
#conn=create_connect(dbpath)
#execute_query(conn,create_gender_table)
#execute_query(conn,insert_gender)
#execute_query(conn,create_users_table)
#execute_query(conn,insert_users)

#insert_user=(input("Eesnimi:"),input("Perenimi"),int(input("Vanus:")),int(input("Sugu:")))
#execute_insert_query(conn,insert_user)

#users=execute_read_query(conn,select_users)
#print("Kautajate tabel 1:")
#for user in users:
#    print(user)
#genders=execute_read_query(conn,select_users_gender)
#print("Kautajate tabel 2:")
#for gender in genders:
#    print(gender)

##------------------------------------------------------------------------------

###from os import *
###from sqlite3 import *
###from sqlite3 import Error

###def create_connection(path:str):
###    connection = None
###    try:
###        connection = connect(path)
###        # print("Ühendus on olemas!")
###    except Error as e:
###        print(f"Tekkis viga: {e}")
###    return connection

###def execute_query(connection, query):
###    try:
###        cursor = connection.cursor()
###        cursor.execute(query)
###        connection.commit()
###        # print("Tabel on loodud.")
###    except Error as e:
###        print(f"Tekkis viga: {e}")

###def read_query(connection, query):
###    cursor = connection.cursor()
###    result = None
###    try:
###        cursor.execute(query)
###        result = cursor.fetchall()
###        return result
###    except Error as e:
###        print(f"Tekkis viga: {e}")

###def drop_table(connection, table):
###    try:
###        cursor = connection.cursor()
###        cursor.execute(f"DROP TABLE IF EXISTS {table}")
###        connection.commit()
###        # print("Tabel on kustutatud.")
###    except Error as e:
###        print(f"Tekkis viga: {e}")

###def columns_from_table(connection, table):
###    cursor = connection.cursor()
###    cursor.execute(f"PRAGMA table_info('{table}')")
###    columnNames = [i[1] for i in cursor.fetchall()]
###    return columnNames

###def find_letter_in_table(connection, table, letter):
###    try:
###        cursor = connection.cursor()
###        column_names = columns_from_table(connection, table)
###        query = f"SELECT * FROM {table} WHERE "
###        conditions = []
###        for column in column_names:
###            conditions.append(f"{column} LIKE '%{letter}%'")
###        query += " OR ".join(conditions)
###        cursor.execute(query)
###        result = cursor.fetchall()
###        return result
###    except Error as e:
###        print(f"Tekkis viga: {e}")

###create_users_table = """CREATE TABLE IF NOT EXISTS Users(
###ID INTEGER PRIMARY KEY AUTOINCREMENT,
###Name TEXT NOT NULL,
###LastName TEXT NOT NULL,
###Gender TEXT NOT NULL,
###Born DATATIME NOT NULL,
###BirthCountry TEXT NOT NULL,
###PassportCountry TEXT NOT NULL)"""

###insert_users = """INSERT INTO Users(Name,LastName,Gender,Born,BirthCountry,PassportCountry) VALUES
###("David","Lennuk","Male","2007-02-25","Estonia","Estonia"),
###("Alinna","Cvetkova","Naine","2007-06-28","Estonia","Estonia"),
###("Timur","Baširov","Male","2005-06-10","Estonia","Estonia"),
###("Igor","Nikolajev","Male","2010-02-24","Russia","Estonia"),
###("Vlad","Kudrashev","Male","2009-03-16","Russia","Estonia")"""

###selectUsers = "SELECT * FROM Users"

###create_cars_table = """CREATE TABLE IF NOT EXISTS Cars(
###ID INTEGER PRIMARY KEY AUTOINCREMENT,
###UsersID INTEGER,
###Mark TEXT NOT NULL,
###Model TEXT NOT NULL,
###Year INTEGER NOT NULL,
###MadeIn TEXT NOT NULL,
###FOREIGN KEY (UsersID) REFERENCES Users(ID))"""

###insert_cars = """INSERT INTO Cars(UsersID,Mark,Model,Year,MadeIn) VALUES
###(3,"Toyota","Corolla",2019,"England"),
###(4,"Toyota","AE86",1986,"Japan"),
###(1,"Nissan","370z",2008,"Japan"),
###(5,"Lada","Riva",2002,"Russia"),
###(2,"Volvo","S80 II",2006,"Sweden")"""

###selectCars = "SELECT Cars.ID,Users.LastName,Cars.Mark,Cars.Model,Cars.Year,Cars.MadeIn FROM Cars INNER JOIN Users ON Cars.UsersID=Users.ID"

###filename = path.abspath(__file__)
###dbDirectory = filename.rstrip('Töö andmebaasiga.py')
###dbPath = path.join(dbDirectory, "data.db")
###connection = create_connection(dbPath)

###execute_query(connection, create_users_table)
###execute_query(connection, insert_users)
###users = read_query(connection, selectUsers)
###execute_query(connection, create_cars_table)
###execute_query(connection, insert_cars)
###users = find_letter_in_table(connection, "Users", "K")
###cars = read_query(connection, selectCars)
###print("Tabel Users:")
###for user in users:
###    print(user)
###print("Tabel Cars:")
###for car in cars:
###    print(car)

#### dropTable(connection, "Users")
#### dropTable(connection, "Cars")
#### users = readQuery(connection, selectUsers)
#### cars = readQuery(connection, selectCars)
#### print(users)
#### print(cars)

###-------------------------------------------------------------------------------------------------------------

##import sqlite3
##from os import path

##def create_connection(db_file):
##    connection = None
##    try:
##        connection = sqlite3.connect(db_file)
##        print("Ühendus on loodud.")
##    except sqlite3.Error as e:
##        print(f"Tekkis viga: {e}")
##    return connection

##def execute_query(connection, query):
##    try:
##        cursor = connection.cursor()
##        cursor.execute(query)
##        connection.commit()
##        print("Päring õnnestus.")
##    except sqlite3.Error as e:
##        print(f"Tekkis viga: {e}")

##def create_tables(connection):
##    create_gender_table = """
##    CREATE TABLE IF NOT EXISTS Gender (
##        ID INTEGER PRIMARY KEY AUTOINCREMENT,
##        Name TEXT NOT NULL
##    )
##    """
##    create_person_table = """
##    CREATE TABLE IF NOT EXISTS Person (
##        ID INTEGER PRIMARY KEY AUTOINCREMENT,
##        Firstname TEXT NOT NULL,
##        Lastname TEXT NOT NULL,
##        Birthdate DATE NOT NULL,
##        Age INTEGER NOT NULL,
##        GenderID INTEGER NOT NULL,
##        FOREIGN KEY (GenderID) REFERENCES Gender(ID)
##    )
##    """
##    execute_query(connection, create_gender_table)
##    execute_query(connection, create_person_table)

##def insert_initial_data(connection):
##    insert_gender_data = """
##    INSERT INTO Gender (Name) VALUES
##    ('Mees'),
##    ('Naine')
##    """
##    execute_query(connection, insert_gender_data)

##def main():
##    db_directory = path.dirname(path.abspath(__file__))
    
##    # Andmebaasi 1: inimese andmed
##    db_person = path.join(db_directory, "person_data.db")
##    connection_person = create_connection(db_person)
##    create_tables(connection_person)
##    insert_initial_data(connection_person)
    
##    # Andmebaasi 2: auto andmed
##    db_car = path.join(db_directory, "car_data.db")
##    connection_car = create_connection(db_car)
##    create_tables(connection_car)
##    insert_initial_data(connection_car)
    
##    connection_person.close()
##    connection_car.close()

##if __name__ == "__main__":
##    main()


#-------------------------------------------------------------------------------
from sqlite3 import connect, Error
from os.path import abspath, dirname, join

def create_connection(path:str):
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
    query = "INSERT INTO users(Name, Lname, Age, GenderId) VALUES(?,?,?,?)"
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()

filename = abspath(__file__)
dbdir = dirname(filename)
dbpath = join(dbdir, "data.db")

create_gender_table = """
CREATE TABLE IF NOT EXISTS gender(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nimetus TEXT NOT NULL
)
"""

create_users_table = """
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Lname TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Residence TEXT NOT NULL,
    Birthday DATETIME NOT NULL,
    GenderId INTEGER,
    FOREIGN KEY (GenderId) REFERENCES gender (Id)
)
"""

insert_gender = "INSERT INTO gender(Nimetus) VALUES('mees'),('naine')"

insert_users = """
INSERT INTO users(Name, Lname, Age, Residence, Birthday, GenderId)
VALUES
    ("David", "Lennuk", 17, "Tallinn", 2007-04-01, 1),
    ("Mark", "Nikolajev", 25, "Tallinn", 1998-06-05, 1),
    ("Alina", "Cvetkova", 39, "Tallinn", 1985-09-10, 2),
    ("Igor", "Aster", 33, "Tallinn", 1980-05-10, 1),
    ("Timur", "Basirov", 19, "Tallinn", 2005-01-15, 1)
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
