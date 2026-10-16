import os
import pickle
import gzip
import threading

DATA_FILE = "students.dat"


def _save(students):
    with gzip.open(DATA_FILE, "wb") as f:   
        pickle.dump(students, f)


def save_data(students):
    t = threading.Thread(target=_save, args=(list(students),))
    t.start()
    return t


def load_data(students):
    if not os.path.exists(DATA_FILE):
        return
    with gzip.open(DATA_FILE, "rb") as f:   
        students.extend(pickle.load(f))