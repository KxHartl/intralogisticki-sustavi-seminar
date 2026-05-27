import matplotlib.pyplot as plt
import numpy as np
import os

# Create images directory if it doesn't exist
os.makedirs('slike', exist_ok=True)

# Data for the chart
years = np.arange(0, 6)
capex_classic = 35000
capex_amr = 125000
opex_classic = 70500
opex_amr = 10300

# Cumulative cost without discounting for simplicity in the chart
cost_classic = capex_classic + opex_classic * years
cost_amr = capex_amr + opex_amr * years

plt.figure(figsize=(10, 6))
plt.plot(years, cost_classic, label='Klasični viličar (3 smjene)', marker='o', linewidth=2, color='#E63946')
plt.plot(years, cost_amr, label='Autonomni viličar (AMR)', marker='s', linewidth=2, color='#1D3557')

# Find intersection point (Payback Period)
# 35000 + 70500*t = 125000 + 10300*t
# 60200*t = 90000 -> t = 1.495
pbp = 90000 / 60200
pbp_cost = capex_classic + opex_classic * pbp

plt.plot(pbp, pbp_cost, 'k*', markersize=12, label=f'Točka pokrića (PBP ≈ 1.5 god)')
plt.axvline(x=pbp, color='gray', linestyle='--')
plt.axhline(y=pbp_cost, color='gray', linestyle='--')

plt.title('Kumulativni troškovi vlasništva (TCO) tijekom 5 godina', fontsize=14, pad=15)
plt.xlabel('Godina', fontsize=12)
plt.ylabel('Kumulativni trošak (EUR)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()

# Save the chart as PDF for LaTeX inclusion
plt.savefig('slike/roi_chart.pdf')
print('Chart generated: slike/roi_chart.pdf')
