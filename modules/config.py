import os
import sqlite3
import langchain

from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate

from langchain_core.callbacks import StreamingStdOutCallbackHandler, CallbackManager
from langchain.callbacks.base import BaseCallbackHandler
from dotenv import load_dotenv

load_dotenv()

Mistral_Model = os.getenv('MISTRAL')

callback_manager = StreamingStdOutCallbackHandler()

# Définition du chemin racine du projet
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

# Définition des répertoires
CONFIG_DIR = os.path.join(ROOT_DIR, "config")
DATA_DIR = os.path.join(ROOT_DIR, "data")
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

# Fichiers de configuration
DATABASE_CONFIG = os.path.join(CONFIG_DIR, "db/db.ini")

# Création des répertoires s'ils n'existent pas
for d in [CONFIG_DIR, DATA_DIR, LOGS_DIR]:
    if not os.path.exists(d):
        os.makedirs(d)


llm = LlamaCpp(
    model_path=Mistral_Model,
    temperature=0.35,
    n_threads=8,
    top_p=1,
    n_ctx=4096,
    n_batch=4096,
    callback_manager=callback_manager,
    n_gpu_layers=3,
    stop=["[INST]"],
    f16_kv=True,
    verbose=True,
    streaming=True,
)



db = sqlite3.connect(DATABASE_CONFIG)


