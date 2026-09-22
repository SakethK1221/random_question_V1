import random


def rand_draw(n_list, q_list, rng=None):
    """Choose one name and one question from the supplied candidates."""
    chooser = rng or random
    chosen_name = chooser.choice(n_list)
    chosen_question = chooser.choice(q_list)
    return chosen_name, chosen_question