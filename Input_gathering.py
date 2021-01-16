def data_inputs():
    link_of_main_page = input("Zadej link na oblast, kterou chceš analyzovat:\n")
    name_of_file = input("Zadejte název souboru, který chcete vytvořit:\n")
    name_of_directory = input("Zadejte název nově vytvořené složky kam se budou data ukládat:\n")
    return link_of_main_page, name_of_file, name_of_directory

if __name__ == "__main__":
    print("Module works")
