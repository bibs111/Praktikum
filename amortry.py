userpass={'icljaya':'semangat'}
userid=input("Masukkan username : ")
password=input("Masukkan Password : ")
if userid in userpass and password==userpass[userid]:
    print("Login berhasil\n")
else:
    print("Login gagal")
    quit()

print("="*50)
print('Selamat datang dikalkulator amortisasi')
print('='*50)

print('\nBerikut ini adalah pilihan periode pembayaran:')
list_periode=['Tahunan','Tengah Tahunan','Kuartal','Bulanan']
i=1
for index in list_periode:
    print(i,index)
    i+=1
periode_terpilih=int(input('Masukkan pilihan periode pembayaran: '))

jumlah_pinjamanawal=int(input('\nMasukkan jumlah pinjaman awal\t: '))
suku_bunga=float(input('Masukkan suku bunga (persen)\t: '))/100
tenor_pengembalian=int(input('Masukkan tenor pengembalian\t: '))

if periode_terpilih==1:
    q=suku_bunga
    p=tenor_pengembalian
elif periode_terpilih==2:
    q=suku_bunga/2
    p=tenor_pengembalian*2
elif periode_terpilih==3:
    q=suku_bunga/4
    p=tenor_pengembalian*4
else:
    q=suku_bunga/12
    p=tenor_pengembalian*12

pembayaran_perperiode=jumlah_pinjamanawal*q*((1+q)**p)//(((1+q)**p)-1)

z=1
while z<=p:
    bunga_periode=(jumlah_pinjamanawal-pembayaran_perperiode)*q//(1-q)
    if bunga_periode<0:
        x=bunga_periode*-1
    else:
        x=bunga_periode
    pokok_bayar=pembayaran_perperiode-x
    print('\nAngsuran pokok periode ',z,': Rp.',int(pokok_bayar))
    print('Angsuran bunga periode ',z,': Rp.',int(x))
    sisa_hutang=jumlah_pinjamanawal-pokok_bayar
    jumlah_pinjamanawal=sisa_hutang
    z+=1

print('\nPembayaran perperiode\t: Rp.',int(pembayaran_perperiode))
print('Total angsuran\t\t: Rp.',int(pembayaran_perperiode*p),'\n')