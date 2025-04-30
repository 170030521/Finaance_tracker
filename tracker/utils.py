import json
import csv
from .decorators import log

@log
def load_from_file(filepath):
    with open(filepath, "r") as f:
        data = json.load(f) 
    return data    

@log
def save_to_file(filepath,data):
    read=load_from_file(filepath)
    read.append(data)
    with open(filepath,"w") as f:
        json.dump(read,f,indent=4)

#this is json file
@log
def delete_from_file(filepath):
    read=load_from_file(filepath)
    read.pop(0)
    with open(filepath,"w") as f:
        json.dump(read,f,indent=4)

# this is for csv file
@log
def write_csv_file(filepath,data):
    with open(filepath,"w",newline="") as f:
        writer=csv.writer(f)
        writer.writerows(data)


# def open        
       



# def read_csv_file():

# def append_csv_file():

# def delete_csv_file():




    

