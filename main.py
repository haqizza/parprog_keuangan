import os
import json

path = os.getcwd()

with open('data.txt', 'rt') as json_file:
   data = json.load(json_file)

import json

data = {}
data['pengeluaran'] = []
data['pengeluaran'].append({
    'nama': 'Pembelian Scott',
    'jumlah': '10000'
})
data['pengeluaran'].append({
    'nama': 'Pembelian Rumah',
    'jumlah': '1000000000'
})
data2 = {}
data2['pemasukan'] = []
data2['pemasukan'].append({
    'nama': 'Hadiah Scott',
    'jumlah': '10000'
})
data2['pemasukan'].append({
    'nama': 'Hibah',
    'jumlah': '1000000'
})

with open(path,'\data.txt', 'w') as outfile:
    json.dump(data,outfile)

with open('d:/GitHub/Parprog/12-12/data.txt', 'a') as outfile: #Just Add
    json.dump(data2,outfile)

with open('data.txt', 'rt') as json_file:
   datas = json.load(json_file)

print(data2["pemasukan"])
print(data["pengeluaran"])
