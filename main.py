import sqlite3
from sqlite3.dbapi2 import Cursor

#function to print db rows
def printdata(rowlist):
    for row in rowlist:
        print(row)
    return


connection = sqlite3.connect("maindatabase.db")
dbcursor = connection.cursor()


command = """CREATE TABLE IF NOT EXISTS  movies (
	Id integer PRIMARY KEY AUTOINCREMENT,
   	moviename Text NOT NULL,
     release_year Integer,
	lead_actor Text,
    lead_actress Text,
    director Text
)"""
dbcursor.execute(command)
connection.commit()

# command = "INSERT INTO movies (moviename,release_year,lead_actor,lead_actress,director) VALUES ('KGF',2018,'Yash','ShreeNidhi Shetty','Prashanth Neel')"
# dbcursor.execute(command)

# command = "select * from movies"
# dbcursor.execute(command)
# print(dbcursor.fetchall())


while True:
    print("""
Please make a choice:
1. Print all data
2. Print based on movie name
3. Print based on actor name
4. Print based on actress name
5. Print based on Director name
6. Print based on Release year
7. Insert New data
    """)

    choice = int(input("> "))

    if choice == 1:
        command = "SELECT * FROM movies"
        dbcursor.execute(command)
        printdata(dbcursor.fetchall())
    elif choice == 2:
        moviename = input("Enter the movie name - ")
        command = f"SELECT * FROM movies WHERE moviename like '%{moviename}%'"
        dbcursor.execute(command)
        printdata(dbcursor.fetchall())
    elif choice == 3:
        lead_actor = input("Enter the lead_actor name - ")
        command = f"SELECT * FROM movies WHERE lead_actor like '%{lead_actor}%'"
        dbcursor.execute(command)
        printdata(dbcursor.fetchall())
    elif choice == 4:
        lead_actress = input("Enter the lead_actress name - ")
        command = f"SELECT * FROM movies WHERE lead_actress like '%{lead_actress}%'"
        dbcursor.execute(command)
        printdata(dbcursor.fetchall())
    elif choice == 5:
        director = input("Enter the director name - ")
        command = f"SELECT * FROM movies WHERE director like '%{director}%'"
        dbcursor.execute(command)
        printdata(dbcursor.fetchall())
    elif choice == 6:
        release_year = input("Enter the movie release_year - ")
        command = f"SELECT * FROM movies WHERE release_year = '{release_year}'"
        dbcursor.execute(command)
        printdata(dbcursor.fetchall())
    elif choice == 7:
        moviename = input("Enter a movie name*: ")
        release_year = int(input("Release year: "))
        lead_actor = input("Lead actor: ")
        lead_actress = input("lead actress: ")
        director = input("Director : ")

        command = f"INSERT INTO movies (moviename,release_year,lead_actor,lead_actress,director) VALUES ('{moviename}',{release_year},'{lead_actor}','{lead_actress}','{director}')"
        dbcursor.execute(command)
        connection.commit()
    else:
        print("Please enter a valid choice ")
