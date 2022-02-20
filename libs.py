import pandas as pd
from os.path import join
from os import getcwd, walk
import sys

"""
pandas used

extension : xlsx, csv


"""


def find_file_in_data(f_n: str, folder_dir: str):
    for i in walk(join(getcwd(), "data")):
        if f_n in i[2]:
            return ".".join([join(getcwd(), "data", folder_dir, f_n)])
    return False


"""
    f_n:str = file name 
    f_d:str = folder_directory
"""


def get_dataframe(f_d: str, f_n: str):

    abs_path = find_file_in_data(f_n, f_d)
    if not abs_path:
        print("존재하지 않는 파일")
        sys.exit()

    ext = f_n.split(".")[-1]
    try:
        return pd.read_csv(abs_path) if ext == "csv" else pd.read_excel(abs_path)
    except Exception as e:
        return (
            pd.read_csv(abs_path, encoding="euc-kr")
            if ext == "csv"
            else pd.read_excel(abs_path, encoding="euc-kr")
        )
