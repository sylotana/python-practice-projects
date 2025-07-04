import json

new_d = {
    'a': 23,
    'b': 42,
    'c': 1231241,
    'd': {1, 2, 3},
    'e': {
        'f': 2,
        'g': 3
    }
}

print(json.dumps(new_d, indent=4, default=str))
