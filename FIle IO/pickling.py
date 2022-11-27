import pickle

# Pickling
# cars = ["Audi" , "BMW" , "Maruti suzuki" , "Harryti Tuziki"]
# file = "FIle IO/mycar.pkl"
# fileobj = open(file, "wb")
# pickle.dump(cars,fileobj)
# fileobj.close()

file = "FIle IO/mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
print(mycar)

# pickle.loads = ?
 