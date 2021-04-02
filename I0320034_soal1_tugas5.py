# input nama dan jenis kelamin pengunjung hotel
nama = str(input('Masukkan nama pengunjung: '))
jenis_kelamin = str(input('Masukkan jenis kelamin: '))

if jenis_kelamin == "Perempuan":
    print('Selamat datang, Nyonya ' + str(nama) + '!')
elif jenis_kelamin == "perempuan":
    print('Selamat datang, Nyonya ' + str(nama) + '!')
elif jenis_kelamin == "wanita":
    print('Selamat datang, Nyonya ' + str(nama) + '!')
elif jenis_kelamin == "Wanita":
    print('Selamat datang, Nyonya ' + str(nama) + '!')
else:
    print('Selamat datang, Tuan ' + str(nama) + '!')
