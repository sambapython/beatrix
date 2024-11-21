import random
import os
import threading

import pandas as pd
from faker import Faker

fak = Faker()

def get_department_ids():
    df = pd.read_csv('departments.csv')
    return df.id.values

def save_data_into_employee_file(f,i):
    print(threading.active_count())
    row = f"{i},{fak.name()},{random.choice(dept_ids)}"
    f.write(row)
    f.write("\n")
    f.flush()
    
dept_ids = get_department_ids()
try:
    f=open(os.path.join("data","employees.csv"),"w")
    for i in range(47000):
        thr = threading.Thread(target=save_data_into_employee_file, args=(f,i))
        thr.start()
except Exception as err:
    print(err)
finally:
    f.close()
