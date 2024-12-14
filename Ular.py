from Animal import *

class Ular(Animal): 
    def __init__(self, nama, makanan, hidup, berkembang_biak, design_kulit, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design_kulit = design_kulit
        self.racun = racun 

    def cetak_ular(self):
        super().cetak()
        print("Design_kulit \t\t: ", self.design_kulit, "\nRacun \t\t: ", self.racun)


kobra = Ular("Kobra", "Burung", "Padang_rumput", "Bertelur", "Pola_terang", "Berbisa")
kobra.cetak_ular()

piton = Ular("Piton", "Rusa", "Hutan_tropis", "Bertelur", "Pola_bercak", "Tidak_berbisa")
piton.cetak_ular()

viper = Ular("Viper", "Tikus", "Hutan", "Bertelur", "Pola_zigzag", "Berbisa")
viper.cetak_ular()

gaboon = Ular("Gaboon", "Kelinci", "Hutan_tropis", "Melahirkan", "Pola_zigzag", "Berbisa")
gaboon.cetak_ular()



