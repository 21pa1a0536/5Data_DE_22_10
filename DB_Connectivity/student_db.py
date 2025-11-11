import sqlite3
from datetime import datetime

#Decorator for Logging Operations
def logging_info(func):
    def wrapper(*args, **kwargs):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)

        log_entry = f"[{now}] Function {func.__name__} is Executed.\n"
        print(log_entry)
        with open("logs.txt", 'a') as file:
            file.write(log_entry)
        return result
    return wrapper

@logging_info
def create_connection(db_name):
    con = None
    try:
        con = sqlite3.connect(db_name)
        print(f"Connection Created Successfully for : {db_name}")
    except sqlite3.Error as e:
        print(f"Error occured in Creating Connection: {e}")
    return con 
#Return's the Connection Object


@logging_info
def create_table(con):
    try:
        cursor = con.cursor()
        cursor.execute('''
            create table if not exists Students(
                       Roll_No INTEGER PRIMARY KEY, Name TEXT NOT NULL, Branch TEXT NOT NULL, Marks INTEGER NOT NULL
                       )

''')
        con.commit()
        print("Student Table Created Successfully")
    except sqlite3.Error as e:
        print(f"An error occured while creating the Table: {e}")



@logging_info
def Insert_data(con, Roll_No, Name, Branch, Marks):
    try:
        cursor = con.cursor()
        cursor.execute("INSERT INTO Students (Roll_No, Name, Branch, Marks) VALUES (?, ?, ?, ?)",(Roll_No, Name, Branch, Marks))
        con.commit()
        print(f"Student {Name}'s Details Added Successfully")
    except sqlite3.Error as e:
        print(f"Error Occured in adding Student {Name}'s Data: {e}")



@logging_info
def fetch_full_data(con):
    try:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Students")
        rows = cursor.fetchall()
        if(rows):
            for row in rows:
                print(row)
        else:
            print("No Data Found")
            return
        print("Data Fetched Successfully")

    except sqlite3.Error as e:
        print(f"Error occured while Fetching Data: {e}")

@logging_info
def fetch_specific_Row(con, Roll_No):
    try:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Students WHERE Roll_No = ?", (Roll_No,))
        rows = cursor.fetchall()
        if(rows):
            for row in rows:
                print(row)
        else:
            print("No Data Found")
            return
        print("Data Fetched Successfully")

    except sqlite3.Error as e:
        print(f"Error occured while Fetching Data: {e}")




@logging_info
def update_data(con, Roll_No, Name = None, Branch = None, Marks = None):
    try:
        cursor = con.cursor()

        fields = []
        values = []

        if(Name):
            fields.append("Name=?")
            values.append(Name)
        if(Branch):
            fields.append("Branch=?")
            values.append(Branch)
        if(Marks):
            fields.append("Marks=?")
            values.append(Marks)
        
        if(not fields):
            print(f"No Data is given to Update")
            return
        
        values.append(Roll_No)
        #adds roll number (which is used for where clause) is appended at the end of the Values list

        query = f"UPDATE Students SET {", ".join(fields)} WHERE Roll_No = ?"

        '''
        This query is like this:  "UPDATE students SET Name = ?, Marks = ? WHERE Roll_No = ?"  
        (If only Name and Marks are given to Update at Certain given Roll Number)
        '''

        cursor.execute(query, values)
        con.commit()
        print("Given Values Updated Successfully")

    except sqlite3.Error as e:
        print(f"Error occured while Updating Data: {e}")



@logging_info
def delete_data(con, Roll_No):
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM Students WHERE Roll_No = ?",(Roll_No,))
        #The "," after Roll_no makes it a Tuple making it executable.
        con.commit()
        print(f"Student with Roll Number {Roll_No}'s Data Deleted Successfully")
    except sqlite3.Error as e:
        print(f"Error occured while performing Delete operation: {e}")