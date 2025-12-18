def create_write(filename):
    with open(r"C:\Users\jspm\Downloads\iris.csv","w") as f:
        f.write("This is data for histogram")
        print("Added Successfully!!!")

def search_file(filename):
    with open(r"C:\Users\jspm\Downloads\iris.csv","r") as f:
        Found = False
        String = f.read()
        a = input("Enter a string you want to find: ")
        if a in String:
            print("The word exist in file")
            Found = True
        else:
            print("The word does not exist in file")
create_write(r"C:\Users\jspm\Downloads\iris.csv")
search_file(r"C:\Users\jspm\Downloads\iris.csv")      
        