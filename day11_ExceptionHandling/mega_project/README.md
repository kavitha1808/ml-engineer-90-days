
### Student Management System (Mega Project)

## 📌 Project Overview

- This is a menu-driven Student Management System built in Python to demonstrate real-world usage of exception handling.

- The project allows users to:

- Add students and their marks

- View student marks

- Calculate average marks

- Save student data to a file

- Load student data from a file

- Access marks safely using index

- Handle all runtime errors gracefully without crashing


This project is designed as a Day 11 Mega Project for mastering Exception Handling.


---

## 🎯 Objectives

- Apply try, except, finally in a real application

- Handle multiple exception types correctly

- Prevent program crashes due to invalid input

- Demonstrate clean, defensive Python programming

- Build an interview-ready, GitHub-worthy project



---

## 🧠 Concepts Used

- Dictionaries and lists

- Functions

- Loops and menu-driven programs

- File handling (read, write)

- Exception handling

- Input validation



---

## ⚠️ Exceptions Handled

This project intentionally covers multiple Python exceptions:

Exception	- Where it is handled

- ValueError- Invalid numeric input, marks, menu choice
- KeyError -	Student name not found
- IndexError- Invalid mark index
- ZeroDivisionError	- Average calculation with empty marks
- FileNotFoundError	- Loading missing file
- Exception	Unexpected - runtime errors

finally	File closing and menu cycle completion



---

## 📂 File Structure

mega_project/
│
├── student_management_system.py
└── students.txt   (created automatically when saving)


---

## 🧩 Features Explained

➤ Add Student

- Takes student name

- Takes number of subjects

- Validates marks (0–100)

- Stores data in dictionary

Handled Errors:

- Invalid number of subjects

- Invalid marks input



---

➤ View Student Marks

- Fetches marks using student name


Handled Errors:

- Student not found (KeyError)



---

➤ Calculate Average Marks

- Calculates average safely


Handled Errors:

- Student not found

- No marks available (ZeroDivisionError)



---

➤ Save to File

- Saves student data into students.txt


Handled Errors:

- File write errors

- Ensures file is closed using finally



---

➤ Load from File

- Reads student data from file


Handled Errors:

- File not found

- Corrupted file content



---

➤ Access Mark by Index

- Retrieves a specific mark using index


Handled Errors:

- Invalid index

- Invalid student name

- Invalid numeric input



---

## ▶️ How to Run

1. Open terminal / command prompt


2. Navigate to mega_project folder


3. Run:



python student_management_system.py


---


## 🛠️ Possible Enhancements

Replace eval() with safer parsing

Convert file storage to CSV

Add password-protected admin access

Convert to OOP-based design



---

