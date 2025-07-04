name_for_id = {456: 'Bella', 893: 'Caleb', 123: 'John'}


# BAD EXAMPLES
def bad_greeting(id):
    if id in name_for_id:  # bad: dict
        return f'Hi, {name_for_id[id]}'  # bad: dict, 'Hi, ...'
    else:  # bad
        return 'Hi, all!'  # bad: 'Hi, ...'


def better_bad_greeting(id):
    if id in name_for_id:  # bad: dict
        return f'Hi, {name_for_id[id]}'  # bad: dict, 'Hi, ...'
    return 'Hi, all!'  # bad: 'Hi, ...'


# EAFP
# Easier to Ask for Forgiveness than Permission.
def eafp_greeting(id):
    try:
        return f'Hi, {name_for_id[id]}'  # bad: 'Hi, ...'
    except KeyError:
        return 'Hi, all!'  # bad: 'Hi, ...'


# PYTHONIC CODE
def pythonic_greeting(id):
    return f'Hi, {name_for_id.get(id, "all")}!'
