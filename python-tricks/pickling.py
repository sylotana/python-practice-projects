import pickle


shoplistfile = 'shoplist.pkl'

shoplist = ['apple', 'tomato', 'cherry']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)
