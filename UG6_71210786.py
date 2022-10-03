class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLLNC:
    _size = 0
    _head = None
    _tail = None

    def _init_(self):
        self._size = 0
        self._head = None
        self._tail = None
    
    def _len_(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def insert_head(self,norek,nama,saldo):
        rekening_baru = NodeTabungan(norek,nama,saldo)
        if(self.isEmpty()):
            self._head = rekening_baru
            self._tail = rekening_baru
            self._tail.next = None
        elif(not self.isEmpty()):
            rekening_baru.next = self._head
            self._head = rekening_baru
        self._size = self._size + 1

    def delete(self, position):
        if self._size == 0:
            return False
        elif position == 0:
            self.delete(0)
        elif position + 1 >= self._size:
            self.delete(self._size)
        elif position - 1 <= self._size:
            delete_node = self._head
            for i in range(position):
                delete_node = delete_node.next
            helper = self._head
            while helper.next != delete_node:
                helper = helper.next
            helper.next = delete_node.next
            del delete_node
            self._size =- 1

    def print(self):
        if(not self.isEmpty()):
            bantu=self._head
            while(bantu!=None):
                print(bantu.no_rekening,' ',bantu.nama,' ',bantu.saldo,' ',end='')
                bantu=bantu.next
            print()
        elif(self.isEmpty()):
            print(f'Kosong!\n')
    
    def filter(self,min_rek):
        bantu = self._head
        for i in range(self._size):
            if bantu.saldo<=min_rek:
                self.delete(i)
                self._size-=1
            bantu=bantu.next            

    def update(self, bunga):
        if bunga>=0 and bunga<=100:
            bantu=self._head
            bunga=bunga/100
            for i in range(self._size):
                bantu.saldo=bantu.saldo+(bantu.saldo*bunga)
            bantu=bantu.next
        elif bunga!=0 and bunga!=100:
            print('Maaf besaran persen harus diantara 0-100')

sllnc=SLLNC()
sllnc.insert_head(201,"Hanif", 250000)
sllnc.insert_head(110,"Yudha", 150000)
sllnc.print()
sllnc.filter(100)
sllnc.print()
sllnc.update(200)
sllnc.update(50)
sllnc.print()