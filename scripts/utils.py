from datetime import datetime
import pandas as pd
import polars as pl
import os


def multi_replace(text, replaces) -> (str, dict):
    for key in replaces.keys():
        text = text.replace(key, replaces[key])
    return text


def path():
    return f'{os.getcwd().split("/scripts")[0]}/PDBs_releases'


def pd_to_csv(df, path, name):
    dt = datetime.now()
    df.to_csv(f'{path}/{name}/{name}_{dt.strftime("%Y_%m_%d")}.csv', index=False)
    df.to_csv(f'{path}/{name}.csv', index=False)
    print('Save files in:')
    print(f'{path}/{name}/{name}_{dt.strftime("%Y_%m_%d")}.csv')
    print(f'{path}/{name}.csv')
    
    
def pl_to_csv(df, path, name):
    dt = datetime.now()
    df.write_csv(f'{path}/{name}/{name}_{dt.strftime("%Y_%m_%d")}.csv')
    df.write_csv(f'{path}/{name}.csv')
    print('Save files in:')
    print(f'{path}/{name}/{name}_{dt.strftime("%Y_%m_%d")}.csv')
    print(f'{path}/{name}.csv')