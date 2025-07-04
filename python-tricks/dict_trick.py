what_happened_dict = {True: 'yes', 1: 'no', 1.0: 'maybe'}

print(what_happened_dict)
# => {True: 'maybe'}


# Let's find out what's going on.
class AlywasEquals:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)

    def __repr__(self):
        return f'{self.name}'


a = AlywasEquals('a')
b = AlywasEquals('b')

print('a == b', a == b)
print('hash(a) == hash(b)', hash(a) == hash(b))

equals_dict = {a: 1, b: 2}
print(equals_dict)
# => {a: 1, b: 2}


class SharedHash:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return 1

    def __repr__(self):
        return f'{self.name}'


c = SharedHash('c')
d = SharedHash('d')

print('c == d', c == d)
print('hash(c) == hash(d)', hash(c) == hash(d))

hash_dict = {c: 1, d: 2}
print(hash_dict)
# => {c: 1, d: 2}


class SharedEqHash:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return True

    def __hash__(self):
        return 1

    def __repr__(self):
        return f'{self.name}'


e = SharedEqHash('e')
f = SharedEqHash('f')

print('e == f', e == f)
print('hash(e) == hash(f)', hash(e) == hash(f))

shared_eq_hash_dict = {e: 1, f: 2}
print(shared_eq_hash_dict)
# => {e: 2}
