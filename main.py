# main.py

import sys
from modules import core, user_interaction

def main():
    # Demandez des instructions et des tâches à l'utilisateur.
    instructions = user_interaction.ask_question("Entrez des instructions : ")
    tasks = user_interaction.ask_question("Entrez des tâches : ").split(',')

    # Générez du code Python à partir de la description donnée.
    code = core.generate_python_code(instructions)

    # Documentez le code généré.
    documented_code = core.document_code(code)

    # Exécutez le code documenté.
    exec(documented_code)

if __name__ == '__main__':
    main()
