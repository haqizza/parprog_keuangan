import os
import json
import time
from datetime import datetime

# Set now as Today Date
now = datetime.today().strftime('%d-%m-%Y')
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
    print("=====[First Time Setting]=====")
    saldo = int(input("Saldo Awal: Rp."))
    anggaran = int(input("Anggaran Bulanan: RP."))
    simpanan = int(input("Simpan Tabungan: RP."))

    dataDeposit['saldo'] = saldo - simpanan # Assign Value
    dataDeposit['anggaran'] = anggaran
    dataDeposit['simpanan'] = simpanan
    with open(path+'\deposit.json', 'w') as outfile: # Menuliskan data di JSON
        json.dump(dataDeposit,outfile,indent=4)

    config['set'] = True # Set bahwa sudah diatur
    with open(path+'\config.json', 'w') as outfile:
        json.dump(config,outfile,indent=4)
    time.sleep(1) # Delay 1 sec
    main()

def tambahSaldo(now,saldo):
    clear()
    print("=====[Tambah Saldo]=====")
    jumlah = int(input("Jumlah: RP."))
    saldo = saldo + jumlah
    
    dataDeposit['saldo'] = saldo
    with open(path+'\deposit.json', 'w') as outfile:
        json.dump(dataDeposit,outfile,indent=4)
    
    print("[Data Ditambahkan]")
    time.sleep(1)
    main()

def transaksi(now,saldo,anggaran):
    clear()
    print("=====[Transaksi]=====")
    tujuan = input("Tujuan: ")
    jumlah = int(input("Jumlah: RP."))
    tanggal = now

    if((saldo-jumlah) < 0):
        print("[Saldo Tidak Mencukupi]")
        time.sleep(1)
        main()
    else:
        dataPengeluaran["pengeluaran"].append({ # Tambah data
            'tujuan': tujuan,
            'jumlah': jumlah,
            'tanggal': now
        })
        with open(path+'\pengeluaran.json', 'w') as outfile:
            json.dump(dataPengeluaran,outfile,indent=4)

        dataRiwayat["riwayat"].append({
            'jenis': 'Pengeluaran',
            'tujuan': tujuan,
            'jumlah': jumlah,
            'tanggal': now
        })
        with open(path+'\\riwayat.json', 'w') as outfile:
            json.dump(dataRiwayat,outfile,indent=4)

        saldo = saldo - jumlah
        dataDeposit['saldo'] = saldo
        anggaran = anggaran - jumlah
        dataDeposit['anggaran'] = anggaran
        with open(path+'\deposit.json', 'w') as outfile:
            json.dump(dataDeposit,outfile,indent=4)
        
        print("[Data Ditambahkan]")
        time.sleep(1)
        main()


def pengaturan():
    clear()
    print("========================[ MENU ]========================")
    print("|1. Atur Anggaran||2. Simpanan||3. Riwayat||4. Laporan|")
    print("|5. Kembali      ||6. Keluar  |                       |")
    print("========================================================")
    pilih = int(input("Menu: "))

    if(pilih == 1):
        aturAnggaran()
    elif(pilih == 2):
        simpanan()
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
        pengaturan()
    
def main():
    clear()
    saldo = dataDeposit["saldo"]
    anggaran = dataDeposit["anggaran"]
    simpanan = dataDeposit["simpanan"]

    print("================[ MENU ]================")
    print("|1. Transaksi||2. Tambah Saldo||3. Pengaturan||4. Keluar|")
    print("========================================")
    print("Saldo Anda: {}".format(saldo))
    print("Anggaran Bulan Ini: {}".format(anggaran))
    print("Simpanan Anda: {}".format(simpanan))
    pilih = int(input("Menu: "))

    if(pilih == 1):
        transaksi(now,saldo,anggaran)
    elif(pilih == 2):
        tambahSaldo(now,saldo)
    elif(pilih == 3):
        pengaturan()
    elif(pilih == 4):
        exit()
    else:
        print("[Menu Tidak Tersedia]")
        main()

# Eksekusi Pertama
sett = config['set']
if(sett==True):
    main()
else:
    setting() #Akan melakukan setting pertama jika belum
