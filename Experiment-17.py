import math

S = 420            
M = 10             
n = 4              
valid = sorted({i*i + i*j + j*j for i in range(0, 5) for j in range(0, 5)} - {0})[:8]

print('{:>3}{:>8}{:>9}{:>12}{:>10}'.format('N', 'D/R', 'ch/cell', 'Capacity C', 'S/I (dB)'))
for N in valid:
    Q = math.sqrt(3*N)                
    k = S // N                         
    C = M * k * N                      
    si = (Q**n) / 6                    
    print(f'{N:>3}{Q:8.3f}{k:9d}{C:12d}{10*math.log10(si):10.2f}')

req = 18.0         
for N in valid:
    if 10*math.log10((math.sqrt(3*N)**n)/6) >= req:
        print()
        print(f'Smallest cluster size meeting S/I >= {req} dB : N = {N}')
        break

