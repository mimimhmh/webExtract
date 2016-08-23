import pickle

d = dict(name='Bob', age=20, score=88)
with open('dump.txt', 'wb') as f:
    f.write(pickle.dumps(d))

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)