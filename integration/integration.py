import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Integration")
root.geometry("300x350")

#new label and input
#student ID label and entry
label_id = tk.Label(root, text="Student ID")
label_id.pack(pady=(15,5))
entry_id = tk.Entry(root, width=25)
entry_id.pack()

#student name label and entry
label_name = tk.Label(root, text="Student Name")
label_name.pack(pady=(15,5))
entry_name = tk.Entry(root, width=25)
entry_name.pack()

#setting print_student function
def print_student():
    student_id = entry_id.get()
    student_name = entry_name.get()


    print("Student ID: {}".format(student_id))
    print("Student Name: {}".format(student_name))
    print("-"*30)

button_print = tk.Button(root, text="Print", command=print_student)
button_print.pack(pady=15)

#connect to database and build environment
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

#def a create_student()
def create_student():
    student_id = entry_id.get()
    student_name = entry_name.get().lower() # application layer

    cursor.execute("INSERT INTO DB_student (db_student_id, db_student_name) VALUES (?, ?)", (student_id, student_name))
    conn.commit()

    print("Student ID: {}".format(student_id))
    print("Student Name: {}".format(student_name))
    print("-"*30)

button_create = tk.Button(root, text="Create", command=create_student)
button_create.pack(pady=20)

def overview_student():
    cursor.execute('SELECT * FROM DB_student')
    overview = cursor.fetchall()
    print(overview)
    
button_overview = tk.Button(root, text="Overview", command=overview_student)
button_overview.pack(pady=25)

print("hello ")

root.mainloop()