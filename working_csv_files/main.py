# READER

# with open("fighters.csv") as file:
#     file.read()

# using reader 
# from csv import reader
# with open("fighters.csv") as file:
#     csv_fighter = reader(file)

    # for row in csv_fighter:
    #     #each row is a list
    #     print(row)
    
    # next(csv_fighter)
    # for fighter in csv_fighter:
    #     print(f"{fighter[0]} is from {fighter[1]}")

# from csv import reader
# with open("fighters.csv") as file:
#     csv_fighter = reader(file)
#     data = list(csv_fighter)
#     print(data)

# DictReader

from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an OrderDict!
        print(row['Name'])