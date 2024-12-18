from itertools import permutations

# Algoritma Brute Force
def muat_truk_brute_force(paket, kapasitas_truk):
    muatan_terbaik = 0
    urutan_terbaik = None
    
    # Menghasilkan semua permutasi dari paket
    for urutan in permutations(paket):
        muatan_sementara = 0
        for p in urutan:
            if muatan_sementara + p <= kapasitas_truk:
                muatan_sementara += p
            else:
                break
        # Cek apakah muatan ini lebih baik
        if muatan_sementara > muatan_terbaik:
            muatan_terbaik = muatan_sementara
            urutan_terbaik = urutan
    return urutan_terbaik, muatan_terbaik

# Algoritma Greedy
def muat_truk_greedy(paket, kapasitas_truk):
    # Mengurutkan paket dari berat terbesar ke terkecil
    paket.sort(reverse=True)
    muatan_sementara = 0
    paket_terpilih = []
    
    for p in paket:
        if muatan_sementara + p <= kapasitas_truk:
            muatan_sementara += p
            paket_terpilih.append(p)
    
    return paket_terpilih, muatan_sementara

# Contoh Input
paket = [4, 8, 2, 6, 5]  # Berat atau volume paket
kapasitas_truk = 15      # Kapasitas maksimum truk

# Menggunakan Brute Force
urutan_bf, muatan_bf = muat_truk_brute_force(paket, kapasitas_truk)
print("Solusi Brute Force:")
print("Urutan Terbaik:", urutan_bf)
print("Total Muatan:", muatan_bf)

# Menggunakan Greedy
paket_greedy, muatan_greedy = muat_truk_greedy(paket, kapasitas_truk)
print("\nSolusi Greedy:")
print("Paket Terpilih:", paket_greedy)
print("Total Muatan:", muatan_greedy)