import json
import csv
import os 
txt_data = "I like Python"
emp = [["Name,Age"],["Riad",22], ["James", 30]]
file_path = "20-Files/output3.csv"

with open(file_path, "w") as file:
    writer = csv.writer(file)
    for row in emp:
        writer.writerow(row)
    print(f"csv file {file_path} was created")
