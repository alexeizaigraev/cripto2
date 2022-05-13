import datetime
from modules import *
import os, sys, shutil


def main():
    print(f'\n{EMAIL_1=}\n{EMAIL_2=}\n')
    fnames = os.listdir('in_data')
    if fnames:
        for fname in fnames:
            log_data = f'start main {fnames}'
            loger(log_data)
            flag_prefix = check_prefix(fname)
            if not flag_prefix:
                p_yellow(f'-> arhiv {fname}')
                continue
            process(fname)
            loger('\n')
        loger('finish main\n')


main()
