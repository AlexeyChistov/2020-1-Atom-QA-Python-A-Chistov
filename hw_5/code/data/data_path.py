import os


DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
FILES = {}
for file in os.listdir(DATA_PATH):
    if file.endswith(".log"):
        FILES[file] = (os.path.join(DATA_PATH, file))
