import pandas as pd

data = [
    [90,80],
    [50,60],
    [65,70],
]

nama=['Mahasiswa 1','Mahasiswa 2','Mahasiswa 3']
matkul=['Algoritma & Struktur data 2','Matematika Numerik']

df = pd.DataFrame(data, index=nama, columns=matkul)
print(df)
print('\n')

print('Rata- rata nilai untuk setiap matkul :')
Nilai_matkul = df.mean(axis=1)
print(Nilai_matkul)
print('\n')

print('Rata- rata nilai untuk setiap mahasiswa :')
Nilai_mahasiswa = df.mean(axis=1)
print(Nilai_mahasiswa)
print('\n')
 