from cs50 import SQL

# Configure CS50 Library to use SQLite database
db: SQL = SQL("sqlite:///utilities.db")

def create_tables():
    db.execute('CREATE TABLE IF NOT EXISTS "users" ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "username" TEXT NOT NULL, "hash" TEXT NOT NULL)')
    pass

create_tables()