from Animal import *

class Burung(Animal): 
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_bulu, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_bulu = warna_bulu
        self.paruh = paruh

    def cetak_burung(self):
        super().cetak()
        print("warna_bulu \t: ", self.warna_bulu, "\nparuh \t\t: ", self.paruh)


merpati = Burung("Merpati", "Biji-bijian", "Udara", "Bertelur", "Putih", "Pendek_Runcing")
merpati.cetak_burung()

beo = Burung("Beo", "Buah-buahan", "Hutan_tropis", "Bertelur", "Hitam", "Besar_melengkung")
beo.cetak_burung()

cendrawasih = Burung("Cendrawasih", "Buah-buahan", "Hutan_tropis", "Bertelur", "Merah", "Pendek_melengkung")
cendrawasih.cetak_burung()

elang = Burung("Elang", "Ikan", "Hutan", "Bertelur", "Coklat", "Tajam")
elang.cetak_burung()





