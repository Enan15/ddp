from Animal import *

class Ikan(Animal): 
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_sirip, metode_bernapas):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_sirip = jenis_sirip
        self.metode_bernapas = metode_bernapas

    def cetak_ikan(self):
        super().cetak()
        print("Jenis_sirip \t: ", self.jenis_sirip, "\nMetode_bernapas\t: ", self.metode_bernapas)


mas = Ikan("Mas", "Cacing", "Air_tawar", "Bertelur", "Actinopterygii", "Insang")
mas.cetak_ikan()

nila = Ikan("Nila", "Pelet", "Air_tawar", "Bertelur", "Actinopterygii", "Insang")
nila.cetak_ikan()

pari = Ikan("Pari", "Krustasea", "Air_laut", "Bertelur", "Sarcopterygii", "Spirakel")
pari.cetak_ikan()

lele = Ikan("Lele", "Serangga", "Air_tawar", "Bertelur", "Actinopterygii", "Insang")
lele.cetak_ikan()

