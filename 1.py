
mahasiswa = []

nim = str(input('Masukkan NIM : '))
nama = str(input('Masukkan Nama : '))
data_baru = {'NIM':nim,'Nama':nama}
mahasiswa.append(data_baru)

new = str(input('Ingin tambahkan lagi : Y/N'))
Y = data_baru = {'NIM':nim,'Nama':nama}
if new == Y:
    print(data_baru)
else:
    print('Data Mahasiswa'.upper())
for a in mahasiswa:
    print(a['NIM'],':',a['Nama'])