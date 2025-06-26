import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# File to store age details
DATA_FILE = "age_details.txt"

# List to keep session age details
age_details = []

#------Functions------

def dob(birth_date):
    """Transforms a date of birth string (YYYY-MM-DD) into a datetime object."""
    return datetime.strptime(birth_date, "%Y-%m-%d")

def find_age(dob):
    """Finds the age from a datetime dob"""
    present_date = datetime.today()
    determined_age = present_date.year - dob.year
    if(dob.month,dob.day) > (present_date.month, present_date.day):
        determined_age -= 1
    return determined_age

def save_details_to_file (filename,details):
    """Saves an additional details to the text file."""
    with open(filename,"a") as f:
        f.write(details + "\n")

def find_age_gui():
    """runs when the user click the button to find age"""
    dob_input = dob_entry.get()
    try:
        dob_date = dob(dob_input)
        age = find_age(dob_date)
        result_label.config(text=f"Age: {age} years")
        details = f"DOB: {dob_input} => Age: {age} years"
        save_details_to_file(DATA_FILE, details)
        messagebox.showinfo("Success", "Age Evaluated and saved successfully.")
    except ValueError:
        messagebox.showerror("Weak Input", "Please enter the correct DOB in YYYY-MM-DD format.")

