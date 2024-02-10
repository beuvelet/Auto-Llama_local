import ast
import inspect


def generate_python_code(description, project_name, file_path):
    """
    Génère du code Python à partir d'une description donnée.
    :param description: Description du code à générer.
    :param project_name: Nom du projet pour lequel générer le code.
    :param file_path: Chemin du fichier dans lequel enregistrer le code généré.
    :return: Code Python généré.
    """
    
    # Analysez la description en utilisant l'analyseur syntaxique d'AST.
    tree = ast.parse(description)

    # Générez le code Python à partir de l'arbre AST.
    code = compile(tree, "<string>", "exec")

    # Enregistrez le code généré dans le fichier indiqué.
    with open(file_path, "w") as f:
        f.write(code)

    print(f"Code Python généré pour le projet {project_name} dans {file_path}")

    return code


def document_code(code, author, version):
    """
    Documente le code en utilisant des docstrings et des commentaires.
    :param code: Code Python à documenter.
    :param author: Auteur du code.
    :param version: Version du code.
    :return: Code Python documenté.
    """
    # Obtenez les noms des fonctions et des méthodes dans le code.
    functions = [name for name in dir(code) if callable(getattr(code, name))]
    
    # Ajoutez des docstrings aux fonctions et aux méthodes.
    for function in functions:
        if not inspect.isbuiltin(getattr(code, function)):
            docstring = f"""
            Description de la fonction {function}
            Auteur: {author}
            Version: {version}
            """
            setattr(code, function, eval(f"lambda : {docstring}\n{getattr(code, function)}"))

    # Ajoutez des commentaires dans le code
    code_lines = code.split("\n")
    commented_lines = []
    for line in code_lines:
        commented_lines.append(f"# {line}")
    code = "\n".join(commented_lines)
            
    return code

