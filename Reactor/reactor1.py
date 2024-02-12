import matplotlib.pyplot as plt

def tangki_reaktor(F_in, C_in, F_out, V, waktu_simulasi, delta_t):
    # Initial
    t = 0
    C = 0.0
    hasil_simulasi = [(t, C)]

    # Persamaan Reaktor Kontinyu (Ideal)
    while t < waktu_simulasi:
        dCdt = (F_in * (C_in - C) - F_out * C) / V
        C = C + delta_t * dCdt
        t = t + delta_t
        hasil_simulasi.append((t, C))

    return hasil_simulasi

def plot_simulasi(hasil_simulasi):
    # Ekstraksi data
    waktu, konsentrasi = zip(*hasil_simulasi)

    # Plot hasil simulasi
    plt.plot(waktu, konsentrasi)
    plt.xlabel('Waktu')
    plt.ylabel('Konsentrasi')
    plt.title('Simulasi Tangki Reaktor Kontinyu')
    plt.show()

if __name__ == "__main__":
    # Variabel Proses
    F_in = 0.5  # Laju aliran masuk
    C_in = 2.0  # Konsentrasi masuk
    F_out = 0.2  # Laju aliran keluar
    V = 10.0    # Volume tangki
    waktu_simulasi = 20.0  # Waktu simulasi
    delta_t = 1.0  # Langkah waktu simulasi

    # Jalankan simulasi
    hasil_simulasi = tangki_reaktor(F_in, C_in, F_out, V, waktu_simulasi, delta_t)

    # Plot hasil simulasi
    plot_simulasi(hasil_simulasi)
