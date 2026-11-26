def erlang_b(E, m):
    # Blocking probability using the recursive Erlang-B formula
    B = 1.0
    for k in range(1, m + 1):
        B = (E * B) / (k + E * B)
    return B

loads = [2, 5, 10, 20]
channels = [5, 10, 15, 20, 25, 30]
print('Blocking probability (%)')
print('E/m   ' + ''.join(f'{m:>9}' for m in channels))
for E in loads:
    print(f'{E:>5} ' + ''.join(f'{100*erlang_b(E, m):9.3f}' for m in channels))

E, target = 10, 0.02
m = 1
while erlang_b(E, m) > target:
    m += 1
print()
print(f'For E = {E} Erlangs and GoS = {target*100:.0f}% -> channels required = {m}')

