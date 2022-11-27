from csv import writer , DictReader

with open("working_csv_files/cats.csv" , "w") as file:
    headers = ["Name" ,"Breed" , "Age"]
    csv_writer = DictReader(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name" : "Garfield",
        "Breed": "Orange Tabby",
        "Age" : 10
    })