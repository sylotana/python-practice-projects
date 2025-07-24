import pickle
from typing import Any

shoplistfile = 'shoplist.pkl'

shoplist = ['apple', 'tomato', 'cherry']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')  # type: ignore
storedlist = pickle.load(f)
print(storedlist)
