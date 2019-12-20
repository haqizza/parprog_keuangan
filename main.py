import os

path = os.getcwd()

global nim,nama,jurusan,kelas

pemasukan = []
pengeluaran = []
jurusan = ["Ilmu Komputer","Ilmu Komputer","Ilmu Komputer"]
kelas = ["C2","C2","C2"]
nim = [1904618,1908653,1904619,1907723]
nama = ["Muhammad Izzatul Haq","Muhamad Fadeelah Rizki","Tatsuya, Hajime","George Washington"]
jurusan = ["Ilmu Komputer","Ilmu Komputer","Ilmu Komputer","Ilmu komputer"]
kelas = ["C2","C2","C2","C2"]
ip = [4,4,3.8]

def lihat_data():
    print("***********************")
    print("   [Data Mahasiswa]")
    for x in range(0,len(nama)):
        print("NIM : {}\nNama : {}\nJurusan: {}\nKelas : {}\nIP : {}".format(nim[x],nama[x],jurusan[x],kelas[x],ip[x]))
        print("---------------")    
    print("***********************")

def cari_data():
    print("***********************")
    print(" [Cari Data Mahasiswa]")
    print("1. NIM\n2. Nama\n3. Jurusan\n4. Kelas")
    acc = int(input("Cari menurut : "))
    if acc == 1:
        src = int(input("Masukkan NIM : "))
        print("---------------")
        for x in range(0,len(nama)):
            if src == nim[x]:
                print("NIM : {}\nNama : {}\nJurusan: {}\nKelas : {}\nIP : {}".format(nim[x],nama[x],jurusan[x],kelas[x],ip[x]))
                print("---------------")
    elif acc == 2:
        src = input("Masukkan Nama : ")
        for x in range(0,len(nama)):
            if src == nama[x]:
                print("NIM : {}\nNama : {}\nJurusan: {}\nKelas : {}\nIP : {}".format(nim[x],nama[x],jurusan[x],kelas[x],ip[x]))
                print("---------------")
    elif acc == 3:
        src = input("Masukkan Jurusan : ")
        for x in range(0,len(nama)):
            if src == jurusan[x]:
                print("NIM : {}\nNama : {}\nJurusan: {}\nKelas : {}\nIP : {}".format(nim[x],nama[x],jurusan[x],kelas[x],ip[x]))
                print("---------------")
    elif acc == 4:
        src = input("Masukkan Kelas : ")
        for x in range(0,len(nama)):
            if src == kelas[x]:
                print("NIM : {}\nNama : {}\nJurusan: {}\nKelas : {}\nIP : {}".format(nim[x],nama[x],jurusan[x],kelas[x],ip[x]))
                print("---------------")

def tambah_data():
    print("***********************")
    print("[Tambah Data Mahasiswa]")
    input_nim = int(input("NIM : "))
    input_nama = input("Nama : ")
    input_jurusan = input("Jurusan : ")
    input_kelas = input("Kelas : ")
    input_ip = input("IP : ")
    nim.extend([input_nim])
    nama.extend([input_nama])
    jurusan.extend([input_jurusan])
    kelas.extend([input_kelas])
    ip.extend([input_ip])
    print("DATA TELAH DITAMBAHKAN")
    print("***********************")

def hapus_data():
    print("***********************")
    print("[Hapus Data Mahasiswa]")
    src = int(input("Masukkan NIM yang akan dihapus : "))
    for x in range(0,len(nama)):
        if src == nim[x]:
            hapus = x
    del nim[hapus]
    del nama[hapus]
    del jurusan[hapus]
    del kelas[hapus]
    del ip[hapus]
    print("DATA TELAH DIHAPUS")
    print("***********************")

def ubah_data():
    print("***********************")
    print(" [Ubah Data Mahasiswa]")
    src = int(input("Masukkan NIM Mahasiswa: "))
    for x in range(0,len(nama)):
        if src == nim[x]:
            edit = x
    input_nim = int(input("NIM : "))
    input_nama = input("Nama : ")
    input_jurusan = input("Jurusan : ")
    input_kelas = input("Kelas : ")
    input_ip = input("IP : ")
    del nim[edit]
    del nama[edit]
    del jurusan[edit]
    del kelas[edit]
    del ip[edit]
    nim.insert(edit,input_nim)
    nama.insert(edit,input_nama)
    jurusan.insert(edit,input_jurusan)
    kelas.insert(edit, input_kelas)
    ip.insert(edit, input_ip)
    print("DATA TELAH DIUBAH")
    print("***********************")


def menu():
    loop = True
    while (loop):
        print("     [ MENU ]")
        print("==================")
        print("1. Lihat Data")
        print("2. Cari Data")
        print("3. Tambah Data")
        print("4. Ubah Data")
        print("5. Hapus Data")
        print("6. Keluar")
        print("==================\n")
        pilih = int(input("Masukkan Pilihan : "))
        if(pilih == 1):
            lihat_data()
        elif(pilih == 2):
            cari_data()
        elif(pilih == 3):
            tambah_data()
        elif(pilih == 4):
            ubah_data()
        elif(pilih == 5):
            hapus_data()
        elif(pilih == 6):
            exit()

menu()


