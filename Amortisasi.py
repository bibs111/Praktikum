userpass={'icljaya':'123'}
def login():
    if userid in userpass and password==userpass[userid]:
        hasil=True
    else:
        hasil=False
    return hasil

i=3
while i>=1:
    userid=input("Masukkan username : ")
    password=input("Masukkan Password : ")
    hasil=login()
    if hasil==True:
        print("Login Berhasil")
        break
    else:
        i-=1
        print("Login Gagal, Sisa Kesempatan Login Anda adalah:",i)
    while i<=0:
        quit()

print("="*50)
print('Selamat datang dikalkulator amortisasi')
print('='*50)

jumlah_pinjamanawal=int(input('Masukkan jumlah pinjaman awal\t: '))
suku_bunga=float(input('Masukkan suku bunga (persen)\t: '))/100
tenor_pengembalian=int(input('Masukkan tenor pengembalian\t: '))

print('\nBerikut ini adalah pilihan periode pembayaran:')
list_periode=['Tahunan','Tengah Tahunan','Kuartal','Bulanan']
i=1
for index in list_periode:
    print(i,index)
    i+=1
periode_terpilih=int(input('\nMasukkan pilihan periode pembayaran: '))

if periode_terpilih==1:
    bunga=suku_bunga
    periode=tenor_pengembalian
elif periode_terpilih==2:
    bunga=suku_bunga/2
    periode=tenor_pengembalian*2
elif periode_terpilih==3:
    bunga=suku_bunga/4
    periode=tenor_pengembalian*4
else:
    bunga=suku_bunga/12
    periode=tenor_pengembalian*12

pembayaran_perperiode=jumlah_pinjamanawal*bunga*((1+bunga)*periode)//(((1+bunga)*periode)-1)
print('\nPembayaran perperiode\t: Rp.',int(pembayaran_perperiode))
print('Total angsuran\t\t: Rp.',int(pembayaran_perperiode*periode))
z=1
while z<=periode:
    bunga_periode=jumlah_pinjamanawal*bunga
    pokok_bayar=pembayaran_perperiode-bunga_periode
    print('\nAngsuran pokok periode ',z,': Rp.',int(pokok_bayar))
    print('Angsuran bunga periode ',z,': Rp.',int(bunga_periode))
    sisa_hutang=jumlah_pinjamanawal-pokok_bayar
    if sisa_hutang<=0:
        print('Sisa hutang periode    ',z,': Rp. 0')
    else:
        print('Sisa hutang periode    ',z,': Rp.',int(sisa_hutang))
    jumlah_pinjamanawal=sisa_hutang
    z+=1