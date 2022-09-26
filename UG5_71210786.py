from pickle import NONE


class Mobil:
    _merk = ""
    _tipe = ""
    _jenisBahanBakar = NONE
    _kapasitasBBM = NONE

    def _init_(self, merk, tipe, jenisBahanBakar, kapasitasBBM):
        self._merk = merk
        self._tipe = tipe
        self._jenisBahanBakar = jenisBahanBakar
        self._kapasitasBBM = kapasitasBBM

    def getMerk(self,merk):
        self._merk = merk

    def getTipe(self,tipe):
        self._tipe = tipe

    def getMerk(self,jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar

    def getMerk(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM

    def getInfo(self):
        print("Merk :", self._merk)
        print("Tipe :", self._tipe)
        print("Bahan Bakar :", self._jenisBahanBakar)
        print("Kapasitas BBM :", self._kapasitasBBM)

    def isiBBM(self,tiapLiter):
        if self._kapasitasBBM  == None  or self._jenisBahanBakar == None:
            print ("EROR! Kapasitas BBM atau Jenis Bahan Bakar belum diinputkan")
        else :   
            print("Mengisi :",self.get_kapasitasBBM())
            print("Total Harga :",self.get_kapasitasBBM()*tiapLiter)
