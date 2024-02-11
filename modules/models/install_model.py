import os
import subprocess

def download_model(model_name, filename):
    command = f'huggingface-cli download {model_name} {filename} --local-dir modules/models --local-dir-use-symlinks False'
    subprocess.run(command, shell=True)

if __name__ == '__main__':
    # Télécharger le modèle Mistral-7B-Instruction
    model_name = 'TheBloke/Mistral-7B-Instruct-v0.2-GGUF'
    filename = 'mistral-7b-instruct-v0.2.Q5_K_M.gguf'
    download_model(model_name, filename)

    # Télécharger le modèle Mistral-7B-code
    model_name = 'TheBloke/Mistral-7B-Instruct-v0.2-code-ft-GGUF'
    filename = 'mistral-7b-instruct-v0.2-code-ft.Q5_K_M.gguf'
    download_model(model_name, filename)

