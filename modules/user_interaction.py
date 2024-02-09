# modules/user_interaction.py

def ask_question(question):
    """
    Pose une question à l'utilisateur et retourne la réponse.

    :param question: Question à poser.
    :return: Réponse de l'utilisateur.
    """
    response = input(question)
    return response
