import tkinter as tk
from tkinter import messagebox
from Age_calculator import DOB, calculate_AGE,save_record_to_file
from datetime import datetime
import os

# File to store age records
DATA_FILE = "age_records.txt"

# List to keep session age records
age_records = []

#------Functions------

def dob(birth_date):
    """Transforms a date of birth string (YYYY-MM-DD) into a datetime object."""
    return datetime.strptime(birth_date, "%Y-%m-%d")

def find_age(dob):
    """Finds the age from a datetime DOB"""
    present_date = datetime.today()
    determined_age = present_date - dob.year
    if(dob.month,dob.day) > (present_date.month, present_date.day):
        determined_age -= 1
    return determined_age

def save_record_to_file (filename,record):
    """Saves an additional record to the text file."""
    with open(filename,"a") as f:
        f.save(record + "\n")



    






    
    
    
    