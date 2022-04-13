from ast import Index
import time

from cv2 import exp
localtime = time.asctime( time.localtime(time.time()) )
data_angsuran_periodik={}
data_angsuran_periodik2={}
data_total_angsuran=[]
total_bunga=[]
banyak_periode=[]
banyak_pengulangan=[]

#Login
userpass={'icljaya':'123','iclkeren':'456','iclmantap':'789'}
kesempatan=2
while kesempatan>=0:
    userid=input("\nMasukkan username : ")
    password=input("Masukkan Password : ")
    if userid in userpass and password==userpass[userid]:
        print("Login berhasil\n")
        break
    else:
        print("Login gagal. Silahkan coba lagi.\nSisa kesempatan Anda: ",kesempatan,'\n')
    kesempatan-=1
    if kesempatan<0:
        print('Maaf Anda tidak bisa mengakses program\n')
        quit()

print("="*50)
print('Selamat datang dikalkulator amortisasi')
print('='*50)

#Kalkulator
pengulangan=0
while pengulangan==0:

    #Input
    while True:
        try:
            jumlah_pinjamanawal=int(input('\nMasukkan jumlah pinjaman awal\t   : '))
            suku_bunga=float(input('Masukkan suku bunga (persen)\t   : '))/100
            tenor_pengembalian=int(input('Masukkan tenor pengembalian (tahun): '))
        except Exception:
            print('Tolong masukkan angka dan bukan karakter')
        else:
            break

    #pelunasan
    while True:
        pelunasan=input('\nApakah anda ingin melunasi pada waktu tertentu? (yes/no): ')
        if pelunasan=='yes':
            if tenor_pengembalian==1:
                while True:
                    try:
                        pelunasan_input=int(input('\nMasukkan waktu pelunasan (bulan ke-): '))
                        waktu_pelunasan=pelunasan_input
                    except Exception:
                        print('Tolong masukkan angka dan bukan karakter')
                    else:
                        break
                break
            else:
                print('\nBerikut ini bentuk waktu pelunasan yang tersedia:')
                waktu=['Tahun','Bulan']
                nomor=1
                for index in waktu:
                    print(nomor,'.',index)
                    nomor+=1
                while True:
                    while True:
                        try:
                            pilihan_waktu=int(input('Masukkan bentuk waktu pelunasan: '))
                        except Exception:
                            print('Tolong masukkan angka dan bukan karakter')
                        else:
                            break
                    if pilihan_waktu==1:
                        while True:
                            try:
                                pelunasan_input=int(input('Masukkan waktu pelunasan (tahun ke-): '))
                                waktu_pelunasan=pelunasan_input*12
                            except Exception:
                                print('Tolong masukkan angka dan bukan karakter')
                            else:
                                break
                        break
                    elif pilihan_waktu==2:
                        while True:
                            try:
                                pelunasan_input=int(input('Masukkan waktu pelunasan (bulan ke-): '))
                                waktu_pelunasan=pelunasan_input
                            except Exception:
                                print('Tolong masukkan angka dan bukan karakter')
                            else:
                                break
                        break
                    else:
                        print('Tolong masukkan sesuai dengan pilihan yang tersedia')
                break
        elif pelunasan=='no':
            break
        else:
            print('Tolong masukkan sesuai dengan pilihan yang tersedia')
    
    #Menghitung Angsuran per Periode
    bunga=suku_bunga/12
    periode=tenor_pengembalian*12
    pembayaran_perperiode=jumlah_pinjamanawal*bunga*((1+bunga)**periode)//(((1+bunga)**periode)-1)
    print('\nPembayaran perbulan\t: Rp.',int(pembayaran_perperiode))  
    if data_angsuran_periodik=={}:
        data=1
        while data<=periode:
            data_angsuran_periodik[data]=pembayaran_perperiode
            data+=1
            try:
                if data==waktu_pelunasan:
                    data_angsuran_periodik[data]=pembayaran_perperiode*(periode-data)
                    if data_angsuran_periodik[data]==0:
                        data_angsuran_periodik[data]=pembayaran_perperiode
                    break
            except NameError:
                waktu_pelunasan=periode
    else:
        data=1
        while data<=periode:
            if data>int(index in data_angsuran_periodik):
                while int(index in data_angsuran_periodik)<data<=periode:
                    data_angsuran_periodik[data]=pembayaran_perperiode
                    data+=1
                break
            jumlah=data_angsuran_periodik[data]+pembayaran_perperiode
            data_angsuran_periodik2[data]=jumlah
            data+=1
            if data==waktu_pelunasan:
                jumlah=data_angsuran_periodik[data]+pembayaran_perperiode*(periode-data)
                data_angsuran_periodik[data]=jumlah
                break
        
    banyak_periode.clear()

    #Menghitung Total Angsuran
    total_angsuran=pembayaran_perperiode*periode
    print('Total angsuran\t\t: Rp.',int(total_angsuran))
    data_total_angsuran.append(total_angsuran)

    #Menghitung Angsuran Pokok, Angsuran Bunga, dan Sisa Hutang per Periode
    periode_ke=1
    while periode_ke<=periode:
        bunga_periode=jumlah_pinjamanawal*bunga
        total_bunga.append(bunga_periode)
        pokok_bayar=pembayaran_perperiode-bunga_periode
        print('\nAngsuran pokok periode ',periode_ke,': Rp.',int(pokok_bayar))
        print('Angsuran bunga periode ',periode_ke,': Rp.',int(bunga_periode))
        sisa_hutang=jumlah_pinjamanawal-pokok_bayar
        if sisa_hutang<=0:
            print('Sisa hutang periode    ',periode_ke,': Rp. 0')
        else:
            print('Sisa hutang periode    ',periode_ke,': Rp.',int(sisa_hutang))
        jumlah_pinjamanawal=sisa_hutang
        periode_ke+=1
        if periode_ke==waktu_pelunasan:
            print('\nAngsuran pokok periode ',periode_ke,': Rp.', int(sisa_hutang))
            print('Angsuran bunga periode ',periode_ke,': Rp.', int(total_angsuran-(sisa_hutang+sum(total_bunga))))
            print('Sisa hutang periode    ',periode_ke,': Rp. 0')
            break

    #Pengulangan
    while True:
        mengulang=input('\nApakah anda ingin melakukan perhitungan peminjaman lainnya? (yes/no): ').lower()
        if mengulang=='no':
            pengulangan+=1
            break
        elif mengulang=='yes':
            banyak_pengulangan.append(1)
            break
        else:
            print('Tolong masukkan sesuai dengan pilihan yang tersedia')

if sum(banyak_pengulangan)>0:
    #Membandingkan Efektivitas Perhitungan
    while True:
        perbandingan=input('\nApakah anda ingin mengetahui perbandingan pembayaran yang ada lakukan? (yes/no): ').lower()
        if perbandingan=='yes':
            print('\nPerhitungan ke-',data_total_angsuran.index(min(data_total_angsuran))+1,' lebih efektif karena total angsurannya lebih kecil yaitu Rp.',min(data_total_angsuran))
            break
        elif perbandingan=='no':
            break
        else:
            print('Tolong masukkan sesuai dengan pilihan yang tersedia')
        
    #Menampilkan Angsuran Kumulatif per Periode
    while True:
        angsuran_kumulatif=input('\nApakah anda ingin menampilkan angsuran kumulatif tiap periode? (yes/no): ').lower()
        if angsuran_kumulatif=='yes':
            print('\nBerikut ini adalah angsuran kumulatif tiap periode: ')
            for key,value in data_angsuran_periodik.items():
                print('Angsuran Periode',key,': Rp.',value)
            break
        elif angsuran_kumulatif=='no':
            break
        else:
            print('Tolong masukkan sesuai dengan pilihan yang tersedia')
    print('\nBerikut ini adalah total angsuran semua pembayaran: Rp.',sum(data_total_angsuran))

#Menampilkan pengguna dan waktu akses
print('\nTerima kasih telah menggunakan program kami')
print(userid,localtime,'\n')