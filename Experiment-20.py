import numpy as np
W = np.array([[ 1,  1,  1,  1],
              [ 1, -1,  1, -1],
              [ 1,  1, -1, -1],
              [ 1, -1, -1,  1]])

bits = {1: [1, 0, 1, 1], 2: [0, 0, 1, 0], 3: [1, 1, 0, 1]}  
L = W.shape[1]
nbits = 4

def bpsk(b):          # 1 -> +1 , 0 -> -1
    return 2*np.array(b) - 1

tx = np.zeros(nbits*L)
for u, b in bits.items():
    spread = np.repeat(bpsk(b), L) * np.tile(W[u], nbits)
    print(f'User {u} data   : {b}')
    print(f'User {u} spread : {spread.astype(int)}')
    tx += spread
print()
print('Composite transmitted signal:')
print(tx.astype(int))

print()
print('Despreading at receiver:')
for u, b in bits.items():
    corr = (tx * np.tile(W[u], nbits)).reshape(nbits, L).sum(axis=1) / L
    rec = (corr > 0).astype(int)
    status = 'OK' if rec.tolist() == b else 'ERROR'
    print(f'User {u} correlator: {corr}  -> bits {rec.tolist()}  {status}')
