import numpy as np
rng = np.random.default_rng(1)

U, TTI = 6, 2000
mean_snr_db = np.array([25, 20, 15, 10, 5, 0])     
mean_snr = 10**(mean_snr_db/10)

rate = np.log2(1 + mean_snr * rng.exponential(1.0, (TTI, U)))

def jain(x):
    return x.sum()**2 / (len(x) * (x**2).sum())

def simulate(policy):
    served = np.zeros(U)
    avg = np.ones(U)
    for t in range(TTI):
        if policy == 'RR':
            u = t % U
        elif policy == 'MaxCI':
            u = np.argmax(rate[t])
        else:                                 
            u = np.argmax(rate[t] / avg)
        served[u] += rate[t, u]
        inst = np.zeros(U)
        inst[u] = rate[t, u]
        avg = 0.99*avg + 0.01*inst
    return served / TTI

print('{:>10} | '.format('Scheduler') + ' '.join('U{:>5}'.format(i+1) for i in range(U)) + ' |  Total | Jain')
for p in ('RR', 'MaxCI', 'PF'):
    th = simulate(p)
    print(f'{p:>10} | ' + ' '.join(f'{v:6.3f}' for v in th) + f' | {th.sum():6.3f} | {jain(th):.3f}')
