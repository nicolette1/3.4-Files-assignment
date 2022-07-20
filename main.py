__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile


os.chdir("files")
path = os.getcwd()
my_zip_file = os.path.join(os.getcwd(), "data.zip")
my_cache_dir = os.path.join(os.getcwd(), "cache")
# Eventuele andere mogelijkheid:
# my_cache_dir = os.path.abspath("cache")


def clean_cache():
    # creates an empty folder named cache in the current directory
    if os.path.exists("cache"):
        shutil.rmtree("cache")
    os.mkdir("cache")


def cache_zip(zip_file_path, cache_dir_path):
    # zip_file_path = my_zip_file
    # cache_dir_path = my_cache_dir
    with zipfile.ZipFile(zip_file_path, "r") as my_zip:
        my_zip.extractall(cache_dir_path)


def cached_files():
    all_cache_files = []
    for text_file in os.listdir(my_cache_dir):
        filepath = os.path.join(my_cache_dir, text_file)
        all_cache_files.append(filepath)
    return all_cache_files


def find_password(all_cache_files):
    for file_path in all_cache_files:
        with open(file_path, "r") as file:
            # Use file to refer to the file object
            list_lines = file.readlines()
            # readlines geeft een lijst met strings.
            # In elke string 1 regel, eindigend op \n
            for line in list_lines:
                if "password" in line:
                    return line.split(": ")[1][:-1]
                    # andere mogelijkheid:
                    # return line[10:-1]


clean_cache()
cache_zip(zip_file_path=my_zip_file, cache_dir_path=my_cache_dir)
cached_files()
find_password(all_cache_files=cached_files())
