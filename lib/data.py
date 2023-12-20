# pip install SQLAlchemy

# Run path/pythonfile.py to persist your schema and create a session.

# crud methods include:
#  creating records, reading records, select specific columns, ordering \
# limiting, filtering, updating data, and deleting data. 

# session in SQLalchemy provides the interface where SELECT and other queries are made that will return and modify ORM-mapped objects.

# Transactions are a strategy for executing SQL statements via ORM that ensure that they all succeed or fail as a group. 

# 1. SQLAlchemy Model Definition:
# The script defines a Student class that inherits from Base, which is provided by SQLAlchemy's declarative_base() function. This class represents a table in the database.

# Attributes of the Student class:

# id: Integer, primary key.
# name: String, student's name.
# email: String, student's email.
# grade: Integer, student's grade (with a check constraint ensuring it's between 1 and 12).
# birthday: DateTime, student's birthday.
# enrolled_date: DateTime, defaulting to the current date and time when a new record is created.

# 2. Table Constraints:
# PrimaryKeyConstraint: Defines the primary key constraint on the 'id' column.
#      assigns primary key status to a Column
# UniqueConstraint: checks new records to ensure that they do not match existing records at unique Columns.
# CheckConstraint: uses SQL statements to check if new values meet specific criteria.



# 3. Table Index:
# An index named 'index_name' is created on the 'name' column for optimization purposes.

# 4. Database Setup:
# An SQLite in-memory database is created using create_engine('sqlite:///:memory:').
# The Base.metadata.create_all(engine) call creates the table in the database.

# 5. Session and Data Population:
# A session is created using Session = sessionmaker(bind=engine).
# Two Student instances (albert_einstein and alan_turing) are created and added to the session using session.bulk_save_objects().

# 6. Querying the Database:
# Various queries are performed using the SQLAlchemy ORM (Object-Relational Mapping) to retrieve and manipulate data.
# Results are printed for each query, demonstrating different functionalities:
# Querying all students.
# Selecting only certain columns (names).
# Ordering students by name.
# Ordering students by grade in descending order.
# Limiting the number of results.
# Using the first() method to retrieve the oldest student.

# 7. Execution:
# The script runs when the file is executed directly (__name__ == '__main__').
# An SQLite in-memory database is used, and the results of various queries are printed to the console.


