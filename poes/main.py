#%% Import Pyhton Libraries
from poes.model.poes import poes
import numpy as np
from scipy.stats import norm, lognorm, expon, triang, uniform
import matplotlib.pyplot as plt



#%% Test poes function
area = 20 #acres
h = 15 #ft
poro = 0.30
swi = 0.10
boi = 1.25


Poes = poes(area, h, poro, swi, boi)
print(f"POES is: {Poes:.2f} bbl")


#%% Test array values
area = np.array([20, 30, 40, 50, 60])
h = np.array([10, 20, 30, 40, 50])
poro = np.array([0.30, 0.32, 0.25, 0.45, 0.28])
swi = np.array([0.10, 0.15, 0.25, 0.30, 0.32])
boi = np.array([1.15, 1.25, 1.30, 1.18, 1.51])

Poes_array = np.round(poes(area, h, poro, swi, boi), 2)
print(Poes_array)

#%% Generate random values for area - Jesus

# NORMAL DISTRIBUTION

area_norm = norm.rvs(loc=200, scale=50, size=1000)

# Definir valores mínimos y máximos (opcional, si quieres recortar)
area_norm = np.where(area_norm < 0, 0, area_norm)


# LOGNORMAL DISTRIBUTION

area_lognorm = lognorm.rvs(s=50, loc=0, scale=100, size=1000)

# Cortar valores negativos o extremadamente grandes
area_lognorm = np.where(area_lognorm < 0, 0, area_lognorm)


# EXPONENTIAL DISTRIBUTION

# loc=0, scale=50
area_expon = expon.rvs(loc=0, scale=50, size=1000)

# TRIANGULAR DISTRIBUTION

# En scipy: c = modo relativo (entre 0 y 1), loc = inicio, scale = rango
# Dados: c=0.2, loc=50, scale=400
area_tri = triang.rvs(c=0.2, loc=50, scale=400, size=1000)


# UNIFORM DISTRIBUTION

# loc=50, scale=400 → valores entre 50 y 450
area_uni = uniform.rvs(loc=50, scale=400, size=1000)


# Visualización de distribuciones

plt.figure(figsize=(10, 6))

plt.subplot(2, 3, 1)
plt.hist(area_norm, bins=50, color='skyblue')
plt.title("Normal")

plt.subplot(2, 3, 2)
plt.hist(area_lognorm, bins=50, color='lightgreen')
plt.title("Lognormal")

plt.subplot(2, 3, 3)
plt.hist(area_expon, bins=50, color='salmon')
plt.title("Exponencial")

plt.subplot(2, 3, 4)
plt.hist(area_tri, bins=50, color='plum')
plt.title("Triangular")

plt.subplot(2, 3, 5)
plt.hist(area_uni, bins=50, color='gold')
plt.title("Uniforme")

plt.tight_layout()
plt.show()

