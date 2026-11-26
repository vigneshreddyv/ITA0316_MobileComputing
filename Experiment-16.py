import numpy as np

def fspl_db(d_km, f_mhz):
    # Free-space path loss in dB (d in km, f in MHz)
    return 20*np.log10(d_km) + 20*np.log10(f_mhz) + 32.44

Pt_dbm, Gt_db, Gr_db = 43.0, 15.0, 0.0      # BS power, BS gain, MS gain
distances = [0.1, 0.5, 1, 2, 5, 10]          # km

for f in (900, 1800):
    print()
    print(f'Frequency = {f} MHz')
    print('{:>8}{:>12}{:>11}{:>14}'.format('d (km)', 'FSPL (dB)', 'Pr (dBm)', 'Pr (W)'))
    for d in distances:
        L = fspl_db(d, f)
        Pr = Pt_dbm + Gt_db + Gr_db - L
        Pr_w = 10**(Pr/10) / 1000
        print(f'{d:8.1f}{L:12.2f}{Pr:11.2f}{Pr_w:14.3e}')

