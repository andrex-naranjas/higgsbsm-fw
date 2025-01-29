import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("dataframe_electrones.csv")
#Separar columnas para electrones y positrones
ele_e = df["electron_e"].to_numpy()
ele_px = df["electron_px"].to_numpy()
ele_py = df["electron_py"].to_numpy()
ele_pz = df["electron_pz"].to_numpy()
pos_e = df["positron_e"].to_numpy()
pos_px = df["positron_px"].to_numpy()
pos_py = df["positron_py"].to_numpy()
pos_pz = df["positron_pz"].to_numpy()

#separar columnas para quarks b
bquark_e = df["bquark_e_e"].to_numpy()
bquark_px = df["bquark_px_e"].to_numpy()
bquark_py = df["bquark_py_e"].to_numpy()
bquark_pz = df["bquark_pz_e"].to_numpy()
antibquark_e = df["anti_bquark_e_e"].to_numpy()
antibquark_px = df["anti_bquark_px_e"].to_numpy()
antibquark_py = df["anti_bquark_py_e"].to_numpy()
antibquark_pz = df["anti_bquark_pz_e"].to_numpy()

#separar columna de px de Z
Z_px = df["Z_boson_px_e"].to_numpy()

Zmass_squared = pow((ele_e + pos_e),2) - pow((ele_px + pos_px),2) - pow((ele_py + pos_py),2) - pow((ele_pz + pos_pz),2)
Zmass = np.sqrt(Zmass_squared)

Hmass_squared = pow((bquark_e + antibquark_e),2) - pow((bquark_px+ antibquark_px),2) - pow((bquark_py + antibquark_py),2) - pow((bquark_pz + antibquark_pz),2)
Hmass = np.sqrt(Hmass_squared)

Z_px_rec = pos_px + ele_px
Z_py_rec = pos_py + ele_py
Z_pz_rec = pos_pz + ele_pz
Z_e_rec = pos_e + ele_e

H_px_rec = bquark_px + antibquark_px
H_py_rec =  bquark_py + antibquark_py
H_pz_rec =  bquark_pz + antibquark_pz
H_e_rec =  bquark_e + antibquark_e

A0_pz_rec = Z_pz_rec + H_pz_rec
A0_px_rec = Z_px_rec + H_px_rec
A0_py_rec = Z_py_rec + H_py_rec
A0_e_rec=Z_e_rec + H_e_rec


A0mass_squared = pow((Z_e_rec + H_e_rec),2) - pow((Z_px_rec + H_px_rec),2) - pow((Z_py_rec + H_py_rec),2) - pow((Z_pz_rec + H_pz_rec),2)
A0mass = np.sqrt(A0mass_squared)

#cos_theta_rec = (A0_pz_rec)/(pow(A0_e_rec,2) - (pow(A0_px_rec,2) + pow(A0_py_rec,2) + pow(A0_pz_rec,2)))
cos_theta_rec = (A0_pz_rec)/(np.sqrt(pow(A0_e_rec,2) - (pow(A0_px_rec,2) + pow(A0_py_rec,2) + pow(A0_pz_rec,2))))
#cos_theta_rec = A0_pz_rec/(A0_pz_rec + A0_px_rec + A0_py_rec)

plt.hist(cos_theta_rec, bins=50, range=(-1, 1), alpha=0.75, color='green', label='A0 Cos theta')
plt.xlabel("Cos theta")
plt.ylabel("Events")
plt.title("Cosine of theta of A0 boson")
plt.legend()
plt.show()


plt.hist(A0mass, bins=50, range=(270, 320), alpha=0.75, color='green', label='A0 mass')
plt.xlabel("Invariant Mass [GeV]")
plt.ylabel("Events")
plt.title("Invariant Mass of A0 boson")
#plt.title("Invariant Mass of Higgs Boson")
plt.legend()
plt.show()


#HISTOGRAMA MASA Z
plt.hist(Zmass, bins=50, range=(70, 110), alpha=0.75, color='green', label='Z mass')
# plt.hist(h_mass_hist, bins=50, range=(0, 250), alpha=0.75, color='green', label='Higgs Mass')
plt.xlabel("Invariant Mass [GeV]")
plt.ylabel("Events")
plt.title("Invariant Mass of Z boson")
#plt.title("Invariant Mass of Higgs Boson")
plt.legend()
plt.show()

plt.hist(Hmass, bins=50, range=(100, 140), alpha=0.75, color='green', label='H mass')
# plt.hist(h_mass_hist, bins=50, range=(0, 250), alpha=0.75, color='green', label='Higgs Mass')
plt.xlabel("Invariant Mass [GeV]")
plt.ylabel("Events")
plt.title("Invariant Mass of H boson")
#plt.title("Invariant Mass of Higgs Boson")
plt.legend()
plt.show()

# Crear el histograma para los datos originales
bins = np.linspace(np.min(Z_px), np.max(Z_px), 30)  # Usar límites consistentes
plt.hist(Z_px, bins=bins, alpha=0.6, label="Z_px (original)", color="blue", edgecolor="black")

# Calcular y graficar puntos para los valores reconstruidos
bin_centers = 0.5 * (bins[:-1] + bins[1:])  # Centros de los bins
hist_reconstructed, _ = np.histogram(Z_px_rec, bins=bins)  # Contar valores en los bins
plt.plot(bin_centers, hist_reconstructed, "ro", label="Z_px (reconstruido)")  # Puntos en rojo

# Configurar etiquetas, leyenda y mostrar la gráfica
plt.xlabel("Momento en x (GeV/c)")
plt.ylabel("Frecuencia")
plt.title("Comparación: Z_px original y reconstruido")
plt.legend()
plt.grid(True)
plt.show()

'''
# Crear gráfico de dispersión
plt.scatter(Z_px, Z_px_rec, alpha=0.7, color="purple")

# Línea de identidad
max_range = max(np.max(Z_px), np.max(Z_px_rec))
min_range = min(np.min(Z_px), np.min(Z_px_rec))
plt.plot([min_range, max_range], [min_range, max_range], 'r--', label="Identidad")

# Configurar etiquetas
plt.xlabel("Z_px (original) [GeV/c]")
plt.ylabel("Z_px (reconstruido) [GeV/c]")
plt.title("Comparación de Z_px original y reconstruido")
plt.legend()
plt.grid(True)
plt.show()
'''
