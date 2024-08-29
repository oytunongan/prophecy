from cs50 import SQL
import csv

students = []
houses = []
assignments = []

def student_table(students):
    for student in students:
        db.execute("INSERT INTO studentsnew (student_name) VALUES (?)", student)

def house_table(houses):
    houses = set(houses)
    for house in houses:
        db.execute("INSERT INTO houses (house) VALUES (?)", house)

def assign_table(assignments):
    for line in assignments:
        db.execute("INSERT INTO assignments (student_name, house) VALUES (?, ?)", line["student_name"], line["house"])

db = SQL("sqlite:///rosternew.db")

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row["student_name"])
        houses.append(row["house"])
        assignments.append(row)

student_table(students)
house_table(houses)
assign_table(assignments)

x = len(students)
y = len(set(houses))
z = len(assignments)

db.execute("DELETE FROM studentsnew WHERE id > ?", x)
db.execute("DELETE FROM houses WHERE id > ?", y)
db.execute("DELETE FROM assignments WHERE id > ?", z)
