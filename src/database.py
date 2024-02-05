import os
import pickle
from fingerprintGenerator import FingerprintGenerator
class Database:
    def create_database(root_folder):
        db = {}
        files = os.listdir(root_folder)
        for file_name in files:
            print("processing file: ", file_name)
            file_path = os.path.join(root_folder, file_name)
            if file_name.lower().endswith(".wav"):
                fingerprint = FingerprintGenerator.generate_fingerprint(file_path)
                db[file_name] = fingerprint
        return db 

    def save_database(pickle_file_path, db):
        with open(pickle_file_path, 'wb') as pickle_file:
            pickle.dump(db, pickle_file)
        print(f"The dictionary has been saved to {pickle_file_path}")

    def load_database(pickle_file_path):
        with open(pickle_file_path, 'rb') as pickle_file:
            loaded_dict = pickle.load(pickle_file)
        return loaded_dict