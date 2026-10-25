import csv

#with open("employees.csv", "w", newline="") as file:
#    writer = csv.writer(file)

#    writer.writerow(["Name", "Age", "Role"])
#    writer.writerow(["Yohesh", "25", "Gen AI"])
#    writer.writerow(["Arun", "23", "Tester"])

#print("Added data in CSV file successfully")

with open("employees.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)