from collections import deque

class Restoran:
    def __init__(self):
        self.antrian = deque()

    def tambah_antrian(self, nama_pelanggan):
        self.antrian.append(nama_pelanggan)
        print(f'Masukkan Nama Pelanggan : {nama_pelanggan}')
        print(f'"{nama_pelanggan}" berhasil ditambahkan ke antrian')

    def hapus_antrian(self):
        if self.antrian:
            nama_pelanggan = self.antrian.popleft()
            print(f'"{nama_pelanggan}" telah dihapus dari antrian')
        else:
            print('Antrian kosong, tidak ada yang dapat dihapus')

    def status_antrian(self):
        if self.antrian:
            print('Antrian saat ini:')
            for i, nama_pelanggan in enumerate(self.antrian, 1):
                print(f'{i}. {nama_pelanggan}')
        else:
            print('Antrian kosong')

def utama():
    restoran = Restoran()
    
    while True:
        restoran.status_antrian()
        print("\nPilihan:")
        print("1. Tambah Antrian")
        print("2. Hapus Pilihan pertama")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == '1':
            nama_pelanggan = input("Masukkan Nama Pelanggan: ")
            restoran.tambah_antrian(nama_pelanggan)
        elif pilihan == '2':
            restoran.hapus_antrian()
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    utama()
