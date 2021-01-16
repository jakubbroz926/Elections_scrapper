import csv
import os


def creation(filename, fieldnames):
    file = open(f"{filename}.csv", "a+", newline = "", encoding = "UTF-8")
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    file.close()


def row_add(filename, fieldnames, rowdata):
    file = open(f"{filename}.csv", "a+", newline = "", encoding = "UTF-8")
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    pairs = dict(zip(fieldnames, rowdata))
    writer.writerow(pairs)


def file_transfer(filename, path):
    os.rename(f"{filename}.csv", f"{path}/{filename}.csv")


def directory_creation(name_of_directory):
    try:
        os.mkdir(name_of_directory)
    except FileExistsError:
        pass

if __name__ == "__main__":
    print("Module works")
