# from csv import reader,writer

# with open('working_csv_files/fighters.csv') as file:
#     csv_reader = reader(file)
#     fighters = [[s.upper() for s in row] for row in csv_reader]
#     for row in fighters :
#         print(row)

# with open('working_csv_files/screeming_fighters_csv', "w") as file:
#     csv_writer = writer(file)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)

#  DICTREADER

# for some reasons , this code is not working 
from csv import DictReader, writer

with open("working_csv_files/cats.csv" , "w") as file:
    headers = ["Name" ,"Breed" , "Age"]
    csv_writer = DictReader(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name" : "Garfield",
        "Breed": "Orange Tabby",
        "Age" : 10
    })
