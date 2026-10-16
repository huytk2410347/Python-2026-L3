import os
import pickle
import gzip
import threading

DATA_FILE = "students.dat"


def _save(students):
    with gzip.open(DATA_FILE, "wb") as f:     # wb = write binary
        pickle.dump(students, f)


def save_data(students):
    # copy the list so the thread isn't affected if the main program changes it
    t = threading.Thread(target=_save, args=(list(students),))
    t.start()
    return t


def load_data(students):
    if not os.path.exists(DATA_FILE):
        return
    with gzip.open(DATA_FILE, "rb") as f:     # rb = read binary
        students.extend(pickle.load(f))