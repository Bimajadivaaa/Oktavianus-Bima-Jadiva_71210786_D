import json
try :
    mahasiswaBaru = int((input('Masukkan jumlah mahasiswa baru: ')))
    for i in range(mahasiswaBaru):
        namaMahasiswa = input('Masukkan nama Anda: ')
        jumlahHobi = int(input('Masukkan jumlah hobi : '))
        listMahasiswa = list()
        dictMahasiswa = dict()
        dictBiodata = dict()
        listHobi = list()
        for j in range(jumlahHobi):
            hobi = input('Masukkan hobi ke-{}: '.format(str(j + 1)))
            listHobi.append(hobi)
        dictBiodata['Hobi'] = listHobi
        prestasi = input('Masukkan prestasi Anda: ')
        dictBiodata['Prestasi'] = prestasi
        dictMahasiswa['BioData'] = dictBiodata
        listMahasiswa.append(dictMahasiswa)
        
        with open('mahasiswa.json', 'r') as datafile:
            data = json.load(datafile)
            data[namaMahasiswa] = listMahasiswa
        with open('mahasiswa.json', 'w') as datafile:
            json.dump(data, datafile)
        print('=== Data berhasil ditambahkan ===\n')
except :
    print("Error")