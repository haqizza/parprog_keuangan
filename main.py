import os
import json
import time
from datetime import datetime

# Set now as Today Date
now = datetime.today().strftime('%d-%m-%Y')
# Set Path
path = os.getcwd()


with open(path+'\deposit.json') as deposit_file:
   dataDeposit = json.load(deposit_file)
with open(path+'\pemasukan.json') as pemasukan_file:
   dataPemasukan = json.load(pemasukan_file)
with open(path+'\pengeluaran.json') as pengeluaran_file:
   dataPengeluaran = json.load(pengeluaran_file)
with open(path+'\\riwayat.json') as riwayat_file:
   dataRiwayat = json.load(riwayat_file)

simpanan = dataDeposit["simpanan"]


def gunakanSaldo(now,saldo):
    tujuan = input("Tujuan: ")
    jumlah = int(input("Jumlah: RP."))
    tanggal = now

    if((saldo-jumlah) < 0):
        print("[Saldo Tidak Mencukupi]")
        time.sleep(1)
        main()
    else:
        dataPengeluaran["pengeluaran"].append({
            'tujuan': tujuan,
            'jumlah': jumlah,
            'tanggal': now
        })
        with open(path+'\pengeluaran.json', 'w') as outfile:
            json.dump(dataPengeluaran,outfile)

        saldo = saldo - jumlah
        dataDeposit['saldo'] = saldo
        with open(path+'\deposit.json', 'w') as outfile:
            json.dump(dataDeposit,outfile)
        
        print("[Data Ditambahkan]")
        time.sleep(1)
        main()

    
def main():
    saldo = dataDeposit["saldo"]
    anggaran = dataDeposit["anggaran"]

    print("===============================[ MENU ]===============================")
    print("|1. Gunakan Saldo||2. Pengaturan||3. Keluar|")
    print("======================================================================")
    print("Saldo Anda: {}".format(saldo))
    print("Anggaran Anda: {}".format(anggaran))
    pilih = int(input("Menu: "))

    if(pilih == 1):
        gunakanSaldo(now,saldo)
    elif(pilih == 2):
        pengaturan()
    elif(pilih == 3):
        exit()
    else:
        print("Menu Tidak Tersedia")
        main()

main()


