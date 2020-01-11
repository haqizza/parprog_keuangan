import os
import json
import time
from datetime import datetime

# Set dates
now = datetime.today().strftime('%d-%m-%Y') # Assign (tanggal-bulan-tahun) hari ini ke now
date = datetime.today().strftime('%d') # Assign tanggal ke date
month = datetime.today().strftime('%B') # Assign nama bulan ke month
# Set Path
path = os.getcwd()

#Membuka file-file
with open(path+'\config.json') as config:
   config = json.load(config)
with open(path+'\\riwayat.json') as riwayat_file:
   dataRiwayat = json.load(riwayat_file)
with open(path+'\deposit.json') as deposit_file:
   dataDeposit = json.load(deposit_file)
with open(path+'\pemasukan.json') as pemasukan_file:
   dataPemasukan = json.load(pemasukan_file)
with open(path+'\pengeluaran.json') as pengeluaran_file:
   dataPengeluaran = json.load(pengeluaran_file)


#Fungsi untuk membersihkan jendela
def clear():
    __ = os.system('cls')

#Fungsi untuk pengaturan pertama kali
def setting():
    clear()
    print("=======[ First Time Setting ]=======")
    saldo = int(input("Saldo Awal: Rp."))
    anggaran = int(input("Anggaran Bulanan: RP."))
    simpanan = int(input("Simpan Tabungan: RP."))

    dataDeposit['saldo'] = saldo - simpanan # Assign Value
    dataDeposit['anggaran'] = anggaran
    dataDeposit['simpanan'] = simpanan
    with open(path+'\deposit.json', 'w') as outfile: # Menuliskan data di JSON
        json.dump(dataDeposit,outfile,indent=4)
    
    config['set'] = True # Set bahwa sudah diatur
    config['anggaran_tanggal'] = int(date)
    config['anggaran_jumlah'] = anggaran
    with open(path+'\config.json', 'w') as outfile:
        json.dump(config,outfile,indent=4)

    print("[Setting Selesai]")
    time.sleep(1) # Delay 2 sec
    main()

def historyWrite(jenis,asalTujuan,jumlah): # Untuk Menulis Riwayat
    if(jenis=='Pemasukan'):
        AorT='asalDana'
    elif(jenis=='Pengeluaran'):
        AorT='tujuan'

    dataRiwayat["riwayat"].append({
        'jenis': jenis,
        AorT: asalTujuan,
        'jumlah': jumlah,
        'tanggal': now
    })
    with open(path+'\\riwayat.json', 'w') as outfile:
        json.dump(dataRiwayat,outfile,indent=4)

def aturAnggaran(anggaran):
    clear()
    print("=======[ Atur Anggaran Bulanan ]=======")
    print("!! Anggaran Akan Dihitung Mulai Hari Ini !!")
    print("Anggaran Bulanan Anda: {}".format(anggaran))
    jumlah = int(input("Jumlah: RP."))
    
    dataDeposit['anggaran'] = jumlah
    with open(path+'\deposit.json', 'w') as outfile:
        json.dump(dataDeposit,outfile,indent=4)
    
    config['anggaran_tanggal'] = int(date)
    config['anggaran_jumlah'] = anggaran
    with open(path+'\config.json', 'w') as outfile:
        json.dump(config,outfile,indent=4)
    
def tambahSaldo(saldo):
    clear()
    print("=======[ Tambah Saldo ]=======")
    print("Saldo Anda: {}".format(saldo))
    asalDana = input("Asal Dana: ")
    jumlah = int(input("Jumlah: RP."))
    saldo = saldo + jumlah
    
    dataDeposit['saldo'] = saldo
    with open(path+'\deposit.json', 'w') as outfile:
        json.dump(dataDeposit,outfile,indent=4)
    
    dataPengeluaran["pengeluaran"].append({ # Tambah data
            'tujuan': tujuan,
            'asalDana': jumlah,
            'tanggal': now
        })
    with open(path+'\pemasukan.json','w') as outfile:
        json.dump(dataPengeluaran,outfile,indent=4)
    
    historyWrite('Pemasukan',asalDana,jumlah)

    print("[Saldo Ditambahkan]")
    time.sleep(1)
    main()

def tambahSimpanan(simpanan,saldo):
    clear()
    print("=======[ Tambah Simpanan ]=======")
    print("Simpanan Anda: {}".format(simpanan))
    cek = input("Ambil dari Saldo (Y/N)?")
    
    if((cek=='n')or(cek=='N')):
        asalDana = input("Asal Dana: ")
    
    jumlah = int(input("Jumlah: RP."))

    if((cek=='y')or(cek=='Y')):
        saldo = saldo - jumlah
        dataDeposit['saldo'] = saldo
        asalDana = "Saldo"

    simpanan = simpanan + jumlah
    dataDeposit['simpanan'] = simpanan
    with open(path+'\deposit.json', 'w') as outfile:
        json.dump(dataDeposit,outfile,indent=4)
    
    historyWrite('Pemasukan',asalDana,jumlah)

    print("[Simpanan Ditambahkan]")
    time.sleep(1)
    simpanans()

def ambilSimpanan(simpanan):
    clear()
    print("=======[ Ambil Simpanan ]=======")
    print("Simpanan Anda: {}".format(simpanan))
    jumlah = int(input("Jumlah: RP."))
    
    if((simpanan - jumlah)<=0):
        print("[Melebihi Simpanan]")
    else:
        simpanan = simpanan - jumlah
        
        dataDeposit['simpanan'] = simpanan
        with open(path+'\deposit.json', 'w') as outfile:
            json.dump(dataDeposit,outfile,indent=4)

        historyWrite('Pengeluaran','Ambil Simpanan',jumlah)

        print("[Simpanan Diambil]")
        time.sleep(1)
        simpanans()

def simpanans():
    clear()
    simpanan = dataDeposit["simpanan"]
    saldo = dataDeposit["saldo"]
    print("=============[ Simpanan ]==============")
    print("|1. Tambah  ||2. Ambil     |          |")
    print("|3. Kembali ||4. Menu Utama||5. Keluar|")
    print("=======================================")
    print("Simpanan Anda: {}".format(simpanan))
    pilih = int(input("Menu: "))

    if(pilih == 1):
        tambahSimpanan(simpanan,saldo)
    elif(pilih == 2):
        ambilSimpanan(simpanan)
    elif(pilih == 3):
        pengaturan()
    elif(pilih == 4):
        main()
    elif(pilih == 5):
        exit()
    else:
        print("[Menu Tidak Tersedia]")
        time.sleep(1)
        pengaturan()

def riwayat():
    clear()
    print("=======[ Riwayat ]=======")

    fh = open('D:\\riwayat.txt', 'w')
    dataR = dataRiwayat["riwayat"]
    x = 1
    for data in dataR:
        fh.write("{}. [{}]\n".format(x,data["tanggal"]))
        fh.write("Jenis       : {}\n".format(data["jenis"]))

        if(data["jenis"]=="Pemasukan"):
            fh.write("Asal Dana   : {}\n".format(data["asalDana"]))
        else:
            fh.write("Tujuan      : {}\n".format(data["tujuan"]))

        fh.write("Jumlah      : Rp.{}\n".format(data["jumlah"]))
        x = x + 1
    fh.close()

    print("[Data Riwayat Telah Diekstrak ke D:\\riwayat.txt]")
    time.sleep(2)
    pengaturan()

def laporan():
    lenPemasukan = len(dataPemasukan["pemasukan"])
    lenPengeluaran = len(dataPengeluaran["pengeluaran"])
    dataPem = dataPemasukan["pemasukan"]
    dataPeng = dataPengeluaran["pengeluaran"]
    jumlahPem =0
    jumlahPeng =0

    for data in dataPemasukan:
        jumlahPem = jumlahPem + dataPemasukan["pemasukan"][0]["jumlah"]
    
    for data in dataPengeluaran:
        jumlahPeng = jumlahPeng + dataPengeluaran["pengeluaran"][0]["jumlah"]

    print("=======[ Laporan ]=======")
    print("[ Data Anda Bulan Ini ]".format(month))
    print("Pemasukan Anda           : {} Transaksi".format(lenPemasukan))
    print("Pemasukan Anda Sebesar   : Rp.{}".format(jumlahPem))
    print("Pengeluaran Anda         : {} Transaksi".format(lenPengeluaran))
    print("Pengeluaran Anda Sebesar : Rp.{}".format(jumlahPeng))
    pilih = input("Kembali(0): ")

    if(pilih == '0'):
        pengaturan()
    elif(pilih != '0'):
        main()


def transaksi(saldo,anggaran):
    clear()
    print("=======[ Transaksi ]=======")
    tujuan = input("Tujuan: ")
    jumlah = int(input("Jumlah: RP."))
    tanggal = now

    if((saldo-jumlah) < 0):
        print("[Saldo Tidak Mencukupi]")
    else:
        dataPengeluaran["pengeluaran"].append({ # Tambah data
            'tujuan': tujuan,
            'jumlah': jumlah,
            'tanggal': now
        })
        with open(path+'\pengeluaran.json','w') as outfile:
            json.dump(dataPengeluaran,outfile,indent=4)

        historyWrite('Pengeluaran',tujuan,jumlah)

        saldo = saldo - jumlah
        dataDeposit['saldo'] = saldo
        anggaran = anggaran - jumlah
        dataDeposit['anggaran'] = anggaran
        with open(path+'\deposit.json','w') as outfile:
            json.dump(dataDeposit,outfile,indent=4)

        print("[Transaksi Ditambahkan]")
    time.sleep(1)
    main()

def pengaturan():
    clear()
    saldo = dataDeposit["saldo"]
    anggaran = dataDeposit["anggaran"]
    simpanan = dataDeposit["simpanan"]

    print("========================[ MENU ]========================")
    print("|1. Simpanan||2. Atur Anggaran||3. Riwayat||4. Laporan|")
    print("|5. Kembali ||6. Keluar       |                       |")
    print("========================================================")
    pilih = int(input("Menu: "))

    if(pilih == 1):
        simpanans()
    elif(pilih == 2):
        aturAnggaran(anggaran)
    elif(pilih == 3):
        riwayat()
    elif(pilih == 4):
        laporan()
    elif(pilih == 5):
        main()
    elif(pilih == 6):
        exit()
    else:
        print("[Menu Tidak Tersedia]")
        time.sleep(1)
        pengaturan()
    
def main():
    clear()
    saldo = dataDeposit["saldo"]
    anggaran = dataDeposit["anggaran"]
    simpanan = dataDeposit["simpanan"]

    print("===================[ MENU ]===================")
    print("|1. Transaksi||2. Tambah Saldo||3. Pengaturan|")
    print("|4. Keluar   |                               |")
    print("==============================================")
    print("Saldo Anda: {}".format(saldo))
    print("Anggaran Bulan Ini: {}".format(anggaran))
    print("Simpanan Anda: {}".format(simpanan))
    pilih = int(input("Menu: "))

    if(pilih == 1):
        transaksi(saldo,anggaran)
    elif(pilih == 2):
        tambahSaldo(saldo)
    elif(pilih == 3):
        pengaturan()
    elif(pilih == 4):
        exit()
    else:
        print("[Menu Tidak Tersedia]")
        time.sleep(1)
        main()

# Eksekusi Pertama
sett = config['set']
if(sett==True):
    tgl = config['anggaran_tanggal']
    cek = config['anggaran_reset']
    #Jika tanggal sudah sama seperti saat set anggaran, reset anggaran ke awal
    if(tgl!=date):
        config['anggaran_reset'] = True #Menandakan perlu direset nanti
        with open(path+'\config.json', 'w') as outfile:
            json.dump(config,outfile,indent=4)
    else:
        if((tgl==date)and(cek==True)):
            dataDeposit['anggaran'] = config['anggaran_tanggal'] # Reset Anggaran bulanan
            with open(path+'\deposit.json', 'w') as outfile:
                json.dump(dataDeposit,outfile,indent=4)
            
            config['anggaran_reset'] = False #Menandakan sudah direset
            with open(path+'\config.json', 'w') as outfile:
                json.dump(config,outfile,indent=4)
    main()
else:
    setting() #Akan melakukan setting pertama jika belum