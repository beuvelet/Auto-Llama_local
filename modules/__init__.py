# modules/__init__.py 'implémentation des fonctions des modules

from modules.config import llm
from modules.core import generate_python_code, document_code
from modules.data_manager import load_data, save_data, get_file_paths, get_dir_structure
from modules.database import get_user, save_project
from modules.user_interaction import ask_question
# No code changes needed
from modules.web_search import search_all

from modules.utils import load_config, save_config, get_config, set_config, init_project, create_module

llm = llm
generate_python_code = generate_python_code
document_code = document_code
load_data = load_data
save_data = save_data
get_file_paths = get_file_paths
get_dir_structure = get_dir_structure
get_user = get_user
save_project = save_project
ask_question = ask_question
search_all = search_all
load_config = load_config
save_config = save_config
get_config = get_config
set_config = set_config
init_project = init_project
create_module = create_module
