import os
import sys
import time
import torch
from dotenv import load_dotenv
from modules import llm
from modules.core import generate_python_code, document_code
from modules.data_manager import load_data, save_data, get_file_paths, get_dir_structure
from modules.database import get_user, save_project
from modules.user_interaction import ask_question
from modules.config import Config
from modules.utils import load_config, save_config, get_config, set_config, init_project, create_module


load_dotenv()


class ProjectManager:
    def __init__(self):
        self.config = Config()
        self.core = generate_python_code
        self.data_manager = load_data
        self.database = get_user
        self.user_interaction = ask_question
        self.models = self.config.models
        self.current_model = list(self.models.keys())[0]

    def switch_model(self, model_name):
        if model_name in self.models:
            self.current_model = model_name
            print(f'Switched to {model_name} model.')
        else:
            print('Invalid model name.')

    def generate_response(self, user_input):
        model = self.models[self.current_model]
        input_ids = torch.tensor(self.data_manager(user_input)).unsqueeze(0)
        output = model.generate(
            input_ids,
            max_length=self.config.max_length,
            num_beams=self.config.num_beams,
            early_stopping=True,
            pad_token_id=self.config.pad_token_id,
            eos_token_id=self.config.eos_token_id,
            length_penalty=self.config.length_penalty,
            no_repeat_ngram_size=self.config.no_repeat_ngram_size
        )
        output = self.data_manager(output.squeeze().tolist())
        return output

    def run(self):
        while True:
            user_input = self.user_interaction()
            if user_input.lower() == 'exit':
                break
            if user_input.lower() == 'load':
                model_name = input('Enter the model name to load: ')
                self.config.load_model(model_name)
                self.models[model_name].load_state_dict(torch.load(f'models/{model_name}.pth'))
                self.models[model_name].eval()
                self.current_model = model_name
                print(f'Loaded {model_name} model.')
            elif user_input.lower() == 'save':
                model_name = input('Enter the model name to save: ')
                self.config.save_model(model_name)
                torch.save(self.models[model_name].state_dict(), f'models/{model_name}.pth')
                print(f'Saved {model_name} model.')
            elif user_input.lower() == 'switch':
                model_name = input('Enter the model name to switch to: ')
                self.switch_model(model_name)
            else:
                output = self.generate_response(user_input)
                print(output)
