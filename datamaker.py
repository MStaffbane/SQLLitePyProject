import sqlite3


def show_all():
   
    conn = sqlite3.connect('people.db')
    
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM person")
    items = c.fetchall()
    print("{:<6}".format("ID ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

    conn.commit()
    conn.close()

def record(first, last, email):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("INSERT INTO person VALUES (?,?,?)", (first, last, email))

    conn.commit()
    conn.close()

def look_record1(id):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM person WHERE rowid = (?)", (id,))
    items= c.fetchall()
    print("{:<6}".format("Row ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

def look_record2(first):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute('SELECT rowid, * FROM person WHERE first_name LIKE ?',(f'%{first}%',))
    items= c.fetchall()
    print("{:<6}".format("Row ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

def look_record3(last):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM person WHERE last_name LIKE ?",(f'%{last}%',))
    items= c.fetchall()
    print("{:<6}".format("Row ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

def look_record4(email):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM person WHERE email LIKE ?",(f'%{email}%',))
    items= c.fetchall()
    print("{:<6}".format("Row ") + "{:<26}".format("NAME ") + "EMAIL")
    for item in items:
        print("{:<5}".format(item[0]) + " " + "{:<10}".format(item[1]) + " " + "{:<15}".format(item[2]) + item[3])

def delete_record(id):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("DELETE from person WHERE rowid = (?)", (id,))

    conn.commit()
    conn.close()

def ammend_firrecord(first, id):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("UPDATE person SET first_name = ? WHERE rowid = ?", (first, id,))

    conn.commit()
    conn.close()

def ammend_lasrecord(last, id):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("UPDATE person SET last_name = ? WHERE rowid = ?", (last, id,))

    conn.commit()
    conn.close()

def ammend_emarecord(email, id):
    conn = sqlite3.connect('people.db')
    c = conn.cursor()
    c.execute("UPDATE person SET email = ? WHERE rowid = ?", (email, id,))

    conn.commit()
    conn.close()
