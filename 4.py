class Buah:
    def __init__(self, nama, warna, rasa):
        self.__nama = nama
        self.__warna = warna
        self.__rasa = rasa

    def set_nama(self, nama):
        self.__nama = nama

    def set_warna(self, warna):
        self.__warna = warna

    def set_rasa(self, rasa):
        self.__rasa = rasa

    def informasi_buah(self):
        return f"Nama: {self.__nama}, Warna: {self.__warna}, Rasa: {self.__rasa}"

class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.__vitamin = vitamin

    def set_vitamin(self, vitamin):
        self.__vitamin = vitamin

    def informasi_mangga(self):
        return f"{self.informasi_buah()}, Vitamin: {self.__vitamin}"

def main():
    buah = Buah("Apel", "Merah", "Manis")
    print(buah.informasi_buah())

    mangga = Mangga("Mangga", "Kuning", "Manis", "Vitamin C")
    print(mangga.informasi_mangga())

# if __name__ == "__main__":
#     main()
