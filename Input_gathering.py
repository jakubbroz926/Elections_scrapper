def data_inputs():
    link_of_main_page = input("Type the URL of district you want to analyze:\n")
    name_of_file = input("Type name of the file you want to create: \n")
    name_of_directory = input("Type name of directory where your data would be stored:\n")
    return link_of_main_page, name_of_file, name_of_directory

if __name__ == "__main__":
    print("Module works")
elif __name__ == "Input_gathering.py":
    data_inputs()
