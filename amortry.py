import time
localtime = time.asctime( time.localtime(time.time()) )
data_angsuran_periodik={}
data_angsuran_periodik2={}
data_total_angsuran=[]
banyak_periode=[]
pilihan_periode=[]
banyak_pengulangan=[]

userpass={'icljaya':'123','iclkeren':'456','iclmantap':'789'}
kesempatan=2
while kesempatan>=0:
    userid=input("Masukkan username : ")
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

pengulangan=0
while pengulangan==0:
    jumlah_pinjamanawal=int(input('\nMasukkan jumlah pinjaman awal\t: '))
    suku_bunga=float(input('Masukkan suku bunga (persen)\t: '))/100
    tenor_pengembalian=int(input('Masukkan tenor pengembalian\t: '))

    print('\nBerikut ini adalah pilihan periode pembayaran:')
    list_periode=['Tahunan','Tengah Tahunan','Kuartal','Bulanan']
    nomor=1
    for index in list_periode:
        print(nomor,index)
        nomor+=1
    periode_terpilih=int(input('Masukkan pilihan periode pembayaran: '))
    if periode_terpilih==1:
        bunga=suku_bunga
        periode=tenor_pengembalian
    elif periode_terpilih==2:
        bunga=suku_bunga/2
        periode=tenor_pengembalian*2
    elif periode_terpilih==3:
        bunga=suku_bunga/4
        periode=tenor_pengembalian*4
    elif periode_terpilih==4:
        bunga=suku_bunga/12
        periode=tenor_pengembalian*12
    else:
        print("Pilihan tidak tersedia\n")
        quit()
    pilihan_periode.append(periode_terpilih)
    periode_ke=1
    while periode_ke<=periode:
        banyak_periode.append(periode_ke)
        periode_ke+=1

    pembayaran_perperiode=jumlah_pinjamanawal*bunga*((1+bunga)**periode)//(((1+bunga)**periode)-1)
    print('\nPembayaran perperiode\t: Rp.',int(pembayaran_perperiode))
    if data_angsuran_periodik=={}:
        data=1
        while data<=periode:
            data_angsuran_periodik[data]=pembayaran_perperiode
            data+=1
    else:
        data2=1
        for index in data_angsuran_periodik:
            jumlah=data_angsuran_periodik[data2]+pembayaran_perperiode
            data_angsuran_periodik2[data2]=jumlah
            data_angsuran_periodik.update(data_angsuran_periodik2)
            data2+=1
            data_angsuran_periodik2.clear()
            if data2>periode:
                break
        while data2<=periode:
            data_angsuran_periodik[data2]=pembayaran_perperiode
            data2+=1
    banyak_periode.clear()

    total_angsuran=pembayaran_perperiode*periode
    print('Total angsuran\t\t: Rp.',int(total_angsuran))
    data_total_angsuran.append(total_angsuran)

    periode_ke=1
    while periode_ke<=periode:
        bunga_periode=jumlah_pinjamanawal*bunga
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
    mengulang=input('\nApakah anda ingin melakukan perhitungan peminjaman lainnya? (yes/no): ').lower()
    if mengulang=='no':
        pengulangan+=1
    else:
        banyak_pengulangan.append(1)

if sum(banyak_pengulangan)>0:
    if pilihan_periode[0]==pilihan_periode[1]:
        perbandingan=input('\nApakah anda ingin mengetahui perbandingan pembayaran yang ada lakukan? (yes/no): ').lower()
        if perbandingan=='yes':
            print('\nPerhitungan ke-',data_total_angsuran.index(min(data_total_angsuran))+1,' lebih efektif karena total angsurannya lebih kecil yaitu Rp.',min(data_total_angsuran))
        angsuran_kumulatif=input('\nApakah anda ingin menampilkan angsuran kumulatif tiap periode? (yes/no): ').lower()
        if angsuran_kumulatif=='yes':
            print('\nBerikut ini adalah angsuran kumulatif tiap periode: ')
            for key,value in data_angsuran_periodik.items():
                print('Angsuran Periode',key,': Rp.',value)
    print('\nBerikut ini adalah total angsuran semua pembayaran: Rp.',sum(data_total_angsuran))
print('Terima kasih telah menggunakan program kami')
print(userid,localtime,'\n')