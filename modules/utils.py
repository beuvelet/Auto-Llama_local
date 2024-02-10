"""
Fichier utils.py contenant des fonctions utilitaires étendues
"""

import os
import json
from pathlib import Path

config = {}
config_file = "config.json"


def load_config():
    """
    Charge la configuration depuis le fichier config.json
    """
    global config
    if os.path.exists(config_file):
        with open(config_file) as f:
            config = json.load(f)
    else:
        config = {}


def save_config():
    """
    Sauvegarde la configuration dans le fichier config.json
    """
    with open(config_file, "w") as f: 
        json.dump(config, f)


def get_config(key, default=None):
    """
    Obtient la valeur d'une clé de configuration.
    
    :param key: Clé de la configuration à obtenir
    :param default: Valeur par défaut à renvoyer si la clé n'existe pas
    :return: Valeur de la clé de configuration ou valeur par défaut
    """
    return config.get(key, default)


def set_config(key, value):
    """
    Définit la valeur d'une clé de configuration.
    
    :param key: Clé de la configuration à définir
    :param value: Valeur à définir pour la clé de configuration
    """
    config[key] = value
    save_config()


def init_project(project_name):
    """
    Initialise la structure de dossiers pour un nouveau projet
    
    :param project_name: Nom du projet
    """
    # Crée le dossier du projet
    project_dir = Path(project_name)
    project_dir.mkdir(exist_ok=True)
    
    # Crée les sous-dossiers
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "data").mkdir(exist_ok=True)
    (project_dir / "models").mkdir(exist_ok=True)
    
    # Crée le fichier principal
    main_file = project_dir / "main.py"
    main_file.touch(exist_ok=True)
    
    # Crée le fichier de configuration
    config_file = project_dir / "config.json"
    config_file.touch(exist_ok=True)
    
    # Crée le fichier README
    readme_file = project_dir / "README.md"
    with open(readme_file, "w") as f:
        f.write("# " + project_name)


def create_module(module_name):
    """
    Crée un nouveau module Python
    
    :param module_name: Nom du module
    :return: Chemin du fichier créé
    """
    module_dir = Path("src")
    module_file = module_dir / (module_name + ".py")
    module_file.touch()
    return module_file


