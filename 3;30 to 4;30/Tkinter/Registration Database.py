import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to create database if it doesn't exist
def create_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS registration_db")
    conn.close()

# Function to create a table
def create_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="registration_db"
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))''')
    conn.commit()
    conn.close()

# Function to add data to the database
def add_data(name, email, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aftab@786",
        database="registration_db"
    )
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (name, email, password)
                      VALUES (%s, %s, %s)''', (name, email, password))
    conn.commit()
    conn.close()

# Function to handle the registration button click
def register_user():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not name or not email or not password:
        messagebox.showerror('Error', 'All fields are required!')
        return
    
    add_data(name, email, password)
    messagebox.showinfo('Success', 'Registration successful!')
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title('Registration Form')
root.geometry("500x400")

# Create labels and entry widgets
tk.Label(root, text='Name:').grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text='Email:').grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text='Password:').grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=2, column=1, padx=10, pady=5)

# Create register button
register_btn = tk.Button(root, text='Register', command=register_user)
register_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Create database if it doesn't exist
create_database()

# Create table
create_table()

root.mainloop()