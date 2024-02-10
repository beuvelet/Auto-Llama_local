import os
import pickle
import json


def load_data(file_path):
    """
    Charge les données à partir d'un fichier pickle ou json
    """
    file_ext = os.path.splitext(file_path)[1]
    if file_ext == ".pickle":
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                return pickle.load(f)
        else:
            return None
    elif file_ext == ".json":
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
        else:
            return None


def save_data(data, file_path):
    """
    Sauvegarde les données dans un fichier pickle ou json
    """
    file_ext = os.path.splitext(file_path)[1]
    if file_ext == ".pickle":
        with open(file_path, "wb") as f:
            pickle.dump(data, f)
    elif file_ext == ".json":
        with open(file_path, "w") as f:
            json.dump(data, f)

            
def get_file_paths(dir_path):
    """
    Retourne la liste des chemins de tous les fichiers dans un répertoire
    """
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


def get_dir_structure(dir_path):
    """
    Retourne la structure des répertoires et fichiers sous forme d'arbre
    """
    dir_structure = {}
    for root, dirs, files in os.walk(dir_path):
        structure = {}
        for dir in dirs:
            structure[dir] = get_dir_structure(os.path.join(root, dir))
        for file in files:
            structure[file] = None
        dir_structure[os.path.relpath(root, dir_path)] = structure
    return dir_structure

