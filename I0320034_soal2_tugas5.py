# Input nama dan nilai pengguna
nama = str(input('Masukkan nama pengguna: '))
nilai = int(input('Masukkan nilai pengguna: '))

# Konversi nilai
if nilai < 60:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah E')
elif nilai >= 60 and nilai <= 64:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah C')
elif nilai >= 65 and nilai <= 69:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah C+')
elif nilai >= 70 and nilai <= 74:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah B')
elif nilai >= 75 and nilai <= 79:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah B+')
elif nilai >= 80 and nilai <= 84:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah A-')
elif nilai >= 85 and nilai <= 100:
    print('Halo, ' + str(nama) + '! Nilai anda setelah dikonversi adalah A')
else:
    print('Nilai tidak valid')
