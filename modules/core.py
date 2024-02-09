# modules/core.py

import ast
import inspect

def generate_python_code(description):
    """
    Génère du code Python à partir d'une description donnée.

    :param description: Description du code à générer.
    :return: Code Python généré.
    """
    # Analysez la description en utilisant l'analyseur syntaxique d'AST.
    tree = ast.parse(description)

    # Générez le code Python à partir de l'arbre AST.
    code = compile(tree, "<string>", "exec")

    return code

def document_code(code):
    """
    Documente le code en utilisant des docstrings.

    :param code: Code Python à documenter.
    :return: Code Python documenté.
    """
    # Obtenez les noms des fonctions et des méthodes dans le code.
    functions = [name for name in dir(code) if callable(getattr(code, name))]

    # Ajoutez des docstrings aux fonctions et aux méthodes.
    for function in functions:
        if not inspect.isbuiltin(getattr(code, function)):
            docstring = f"Description de la fonction {function}"
            setattr(code, function, eval(f"lambda : {docstring}\n{getattr(code, function)}"))

    return code
