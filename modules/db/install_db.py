import configparser
import mysql.connector
import os
import time

# Définir le chemin absolu du fichier de configuration
config_path = os.path.join(os.path.dirname(__file__), 'db.ini')

# Lire les paramètres de connexion à partir du fichier de configuration
config = configparser.ConfigParser()
config.read(config_path)

# Récupérer les paramètres de connexion à partir du fichier de configuration
db_config = dict(config['mysql'])

# Définir le chemin absolu du fichier SQL
sql_file = 'auto_llama_db.sql'
sql_path = os.path.abspath(os.path.join(os.path.dirname(__file__), sql_file))

# Lire le contenu du fichier SQL
with open(sql_path, 'r') as file:
    sql_script = file.read()

try:
    # Se connecter à la base de données
    cnx = mysql.connector.connect(**db_config)

    # Créer un curseur pour exécuter le script SQL
    cursor = cnx.cursor(buffered=True)

    # Exécuter le script SQL pour installer la base de données et les données
    for command in sql_script.split(';'):
        if command.strip():
            cursor.execute(command)
            cnx.commit()
            time.sleep(0.3)

    print("La base de données et les données ont été installées avec succès.")

except mysql.connector.Error as err:
    print("Erreur lors de l'installation de la base de données:", err)

finally:
    # Fermer le curseur et la connexion
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'cnx' in locals() and cnx is not None:
        cnx.close()
