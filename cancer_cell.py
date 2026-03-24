# ** CELLULAR AUTOMATA - CANCER CELL DEVELOPMENT WITH TP53 MUTATION
# ** Authors: crakshay & georgyzaouk
# ** Paris Saclay University
from cellularautomata import CountType, GuiCA
from random import random, randint

tp53_mutation = 67
division_rate = 0.2

def cancer(cell, neighbors):
    state, data = cell

    # Initialisation
    if data is None:
        data = {'damage': 0.0, 'tp53': True}

    damage = data['damage']
    tp53 = data['tp53']

    # TP53 mutation
    if tp53 and randint(0, 400) == tp53_mutation:
        tp53 = False

    # ================= RULES =================
    if state == 'Normal':
        damage += random() * 0.1
        return ('Damaged', {'damage': damage, 'tp53': tp53})

    elif state == 'Damaged':
        damage += random() * 0.1
        if tp53:
            if damage < 0.2:
                damage = max(0, damage - random()*0.1)
                return ('Normal', {'damage': damage, 'tp53': tp53})

            elif damage < 0.5:
                return ('Damaged', {'damage': damage, 'tp53': tp53})

            else:
                # Apoptosis
                return ('Empty', None)

        else:
            if damage < 0.5:
                return ('Damaged', {'damage': damage, 'tp53': tp53})
            else:
                return ('Cancer', {'damage': damage, 'tp53': tp53})

    elif state == 'Cancer':
        return ('Cancer', {'damage': damage, 'tp53': tp53})

    elif state == 'Empty':
        # Filling the empty cells 
        if random() < CountType(neighbors, 'Cancer') * 0.08:
            return ('Cancer', {'damage': 0.0, 'tp53': False})

        if random() < CountType(neighbors, 'Normal') * 0.05:
            return ('Normal', {'damage': 0.0, 'tp53': True})

        if random() < CountType(neighbors, 'Damaged') * 0.03:
            return ('Damaged', {'damage': 0.1, 'tp53': True})

        return ('Empty', None)

    return cell


# Colors
cellcolors = {
    ('Empty', None): 'white',
    ('Normal', None): 'green',
    ('Damaged', None): 'pink',
    ('Cancer', None): 'red'
}

GuiCA(cancer, cellcolors)