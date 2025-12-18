def create_write(filename):
    with open(r"C:\Users\jspm\Downloads\iris.csv","w") as f:
        f.write("This is data for histogram")
        print("Added Successfully!!!")

create_write(r"C:\Users\jspm\Downloads\iris.csv")

def read(filename):
    with open(r"C:\Users\jspm\Downloads\iris.csv","r") as f:
        print(f.read())

read(r"C:\Users\jspm\Downloads\iris.csv")

def append_and_read(filename,new):
    with open(r"C:\Users\jspm\Downloads\iris.csv","a") as f:
        f.write(new + "\n")
        print("appended!")
        
append_and_read(r"C:\Users\jspm\Downloads\iris.csv","Arnav")