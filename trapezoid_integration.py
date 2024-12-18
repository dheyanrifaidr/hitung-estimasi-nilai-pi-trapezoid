import numpy as np
import time

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode Trapezoid untuk integral numerik
def trapezoid_integration(func, a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = func(x)
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

# Galat RMS
def calculate_rms(errors):
    return np.sqrt(np.mean(np.square(errors)))

# Nilai referensi pi
pi_reference = 3.141592653589793

# Variasi nilai N
N_values = [10, 100, 1000, 10000]
errors = []
execution_times = []

print("\nMetode Trapezoid untuk Menghitung Nilai Pi:\n")
for N in N_values:
    start_time = time.time()
    numerical_result = trapezoid_integration(f, 0, 1, N)
    end_time = time.time()

    error = abs(numerical_result - pi_reference)
    errors.append(error)
    execution_times.append(end_time - start_time)

    print(f"N = {N:6d}, Hasil = {numerical_result:.15f}, Galat = {error:.15e}, Waktu = {end_time - start_time:.6f} detik")

# Menghitung galat RMS
rms_error = calculate_rms(errors)
print(f"\nGalat RMS: {rms_error:.15e}")

# Menyimpan hasil dalam format tabel
import pandas as pd
results = pd.DataFrame({
    'N': N_values,
    'Hasil Numerik': [trapezoid_integration(f, 0, 1, N) for N in N_values],
    'Galat': errors,
    'Waktu Eksekusi (s)': execution_times
})

# Menyimpan ke file CSV
results.to_csv("trapezoid_results.csv", index=False)
print("\nHasil disimpan ke file 'trapezoid_results.csv'.")
