# main.py

import sys
from modules import core, utils, data_manager, config, user_interaction

def main():
    # Demandez des instructions et des tâches à l'utilisateur.
    instructions = user_interaction.ask_question("Entrez des instructions : ")
    tasks = user_interaction.ask_question("Entrez des tâches : ").split(',')

    # Chargez les données à partir du fichier d'entrée.
    input_data = utils.load_data(config.get_config()['input_file'])

    # Traitez les données.
    processed_data = data_manager.process_data(input_data)

    # Générez la sortie.
    output_data = core.generate_output(processed_data, instructions, tasks)

    # Enregistrez les données de sortie dans le fichier de sortie.
    with open(config.get_config()['output_file'], 'w') as file:
        file.write(output_data)

if __name__ == '__main__':
    main()
