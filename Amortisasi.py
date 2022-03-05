
jumlahpinjamanawal=int(input('Masukkan jumlah pinjaman awal : '))
sukubunga=int(input('Masukkan suku bunga (persen) : '))/100
tenorpengembalian=int(input('Masukkan tenor pengembalian : '))

pembayaranperperiode=jumlahpinjamanawal*sukubunga*((1+sukubunga)**tenorpengembalian)//(((1+sukubunga)**tenorpengembalian)-1)
bungaperiode=sisahutang*sukubunga
pokokbayar=pembayaranperperiode-bungaperiode
sisahutang=jumlahpinjamanawal-pokokbayar

print('\nBiaya pokok : ',pokokbayar)
print('Bunga periode : ',bungaperiode)
print('Pembayaran perperiode : ',pembayaranperperiode)
print('Sisa hutang : ',sisahutang)
print('Total angsuran : ',pembayaranperperiode*3,'\n')
