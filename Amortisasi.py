def menu():
    print("1. Tahunan")
    print("2. Tengah Tahunan")
    print("3. Kuartal")
    print("4. Bulanan")
    
def tahunan():
    pembayaranperperiode=jumlahpinjamanawal*sukubunga*((1+sukubunga)**tenorpengembalian)//(((1+sukubunga)**tenorpengembalian)-1)
    bungaperiode=(jumlahpinjamanawal-pembayaranperperiode)*sukubunga//(1-sukubunga)
    pokokbayar=pembayaranperperiode-bungaperiode
    sisahutang=jumlahpinjamanawal-pokokbayar
    print('\nBiaya pokok\t\t: Rp.',int(pokokbayar))
    print('Bunga periode\t\t: Rp.',int(bungaperiode))
    print('Pembayaran perperiode\t: Rp.',int(pembayaranperperiode))
    print('Sisa hutang\t\t: Rp.',int(sisahutang))
    print('Total angsuran\t\t: Rp.',int(pembayaranperperiode*tenorpengembalian),'\n')

def tengahtahunan():
    sukubunga2=sukubunga/2
    periode=tenorpengembalian*2
    pembayaranperperiode=jumlahpinjamanawal*sukubunga2*((1+sukubunga2)**periode)//(((1+sukubunga2)**periode)-1)
    bungaperiode=(jumlahpinjamanawal-pembayaranperperiode)*sukubunga2//(1-sukubunga2)
    pokokbayar=pembayaranperperiode-bungaperiode
    sisahutang=jumlahpinjamanawal-pokokbayar
    print('\nBiaya pokok\t\t: RP.',int(pokokbayar))
    print('Bunga periode\t\t: Rp.',int(bungaperiode))
    print('Pembayaran perperiode\t: Rp.',int(pembayaranperperiode))
    print('Sisa hutang\t\t: Rp.',int(sisahutang))
    print('Total angsuran\t\t: RP.',int(pembayaranperperiode*periode),'\n')

def kuartal():
    sukubunga3=sukubunga/4
    periode2=tenorpengembalian*4
    pembayaranperperiode=jumlahpinjamanawal*sukubunga3*((1+sukubunga3)**periode2)//(((1+sukubunga3)**periode2)-1)
    bungaperiode=(jumlahpinjamanawal-pembayaranperperiode)*sukubunga3//(1-sukubunga3)
    pokokbayar=pembayaranperperiode-bungaperiode
    sisahutang=jumlahpinjamanawal-pokokbayar
    print('\nBiaya pokok\t\t: Rp.',int(pokokbayar))
    print('Bunga periode\t\t: Rp.',int(bungaperiode))
    print('Pembayaran perperiode\t: Rp.',int(pembayaranperperiode))
    print('Sisa hutang\t\t: Rp.',int(sisahutang))
    print('Total angsuran\t\t: Rp.',int(pembayaranperperiode*periode2),'\n')

def bulanan():
    sukubunga4=sukubunga/12
    periode3=tenorpengembalian*12
    pembayaranperperiode=jumlahpinjamanawal*sukubunga4*((1+sukubunga4)**periode3)//(((1+sukubunga4)**periode3)-1)
    bungaperiode=(jumlahpinjamanawal-pembayaranperperiode)*sukubunga4/(1-sukubunga4)
    pokokbayar=pembayaranperperiode-bungaperiode
    sisahutang=jumlahpinjamanawal-pokokbayar
    print('\nBiaya pokok\t\t: Rp.',int(pokokbayar))
    print('Bunga periode\t\t: Rp.',int(bungaperiode))
    print('Pembayaran perperiode\t: Rp.',int(pembayaranperperiode))
    print('Sisa hutang\t\t: Rp.',int(sisahutang))
    print('Total angsuran\t\t: Rp.',int(pembayaranperperiode*periode3),'\n')

# Program Utama
print("="*50)
print("Selamat Datang di Program Perhitungan Amortisasi")
print("="*50)

# Input
jumlahpinjamanawal=int(input('Masukkan jumlah pinjaman awal\t: '))
sukubunga=float(input('Masukkan suku bunga (persen)\t: '))/100
tenorpengembalian=int(input('Masukkan tenor pengembalian\t: '))
print("Berikut Merupakan Pilihan Periode Pembayaran:")
menu()
pilih=input("Masukkan Pilihan Periode Pembayaran: ")
if pilih == ("1"):
    tahunan()
elif pilih == ("2"):
    tengahtahunan()
elif pilih == ("3"):
    kuartal()
elif pilih == ("4"):
    bulanan()