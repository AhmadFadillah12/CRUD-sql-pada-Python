import sqlite3
import os

conn = sqlite3.connect('dbsisfodik.db')
c = conn.cursor()

def lihat_data():
    no = 0
    data = c.execute('select * from mahasiswa')
    print('Data Mahasiswa')
    print('---------------------')
    for baris in data:
        no += 1
        print(str(no), baris[0], baris[1])
    print('---------------------')

def tambah_data():
    lihat_data()
    nim            = input('Masukkan NIM  : ')
    nama           = input('Masukkan Nama : ')
    data_mahasiswa = [nim, nama]
    c.execute('insert into mahasiswa (nim, nama) values (?,?)', data_mahasiswa)
    conn.commit()
    print('\n')

def edit_data():
    lihat_data()
    nim_rubah = input('Rubah data NIM : ')
    nim       = input('Masukkan NIM   : ')
    nama      = input('Masukkan Nama  : ')
    data_mahasiswa = [nim, nama]
    c.execute('update mahasiswa set nim = ?, nama = ?', data_mahasiswa)
    conn.commit()
    print('\n')

def hapus_data():
    lihat_data()
    nim_hapus = input('Hapus data NIM : ')
    data_mahasiswa = [nim_hapus]
    c.execute('delete from mahasiswa where nim = ?', data_mahasiswa)
    conn.commit()
    print('\n')

os.system('cls')
loop = True
while loop:
    print('Pilih perintah')
    print('----------------------------')
    print('1. Lihat data')
    print('2. Tambah data')
    print('3. Edit data')
    print('4. hapus data')
    print('5. Keluar')
    pilih = int(input('Input Pilihan dalam angka 1-5 : '))
    os.system('cls')
    if pilih == 1:
        lihat_data()
    elif pilih == 2:
        tambah_data()
    elif pilih == 3:
        edit_data()
    elif pilih == 4:
        hapus_data()
    else:
        loop = False