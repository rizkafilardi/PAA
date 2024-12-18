from itertools import permutations

def muat_truk_brute_force (paket, kapasitas_truk):
    muatan_terbaik = 0
    urutan_terbaik = None

    #algoritma permutasi
    for urutan in permutations (paket):
        muatan_sementara = 0
        for p in urutan : 0
        
        if muatan_sementara + p <= kapasitas_truk:
            muatan_sementara +=p
        else:
            break

    #cek apakah muatan lebih baik
    if muatan_sementara < kapasitas_truk:
        muatan_terbaik = muatan_sementara
        urutan_terbaik = urutan
    return urutan_terbaik, muatan_terbaik

#algoritma greedy
def muat_truk_greedy (paket, kapasitas_truk):
    paket.sort(reserve=True)
    muatan_terbaik=0
    paket_terpilih=[]

    for p in paket:
        if muatan_sementara + p <= kapasitas_truk:
            muatan_sementara +=p 

            paket_terpilih.append(p)
    return paket_terpilih, muatan_sementara

#contoh input
paket = [4, 8, 2, 6, 5]
kapasitas_truk = 15





 